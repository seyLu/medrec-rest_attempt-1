#!/usr/bin/env python

"""
1. retrieve from api (region, province, city, district)
2. create corresponding json fixtures

pseudocode:
get region 8
take code

get all provinces with code=<region_code>
for each provinces
    take code
    get all cities-municipalities with code=<province_code>

        for each cities-municipalities
            take code
                get all districts with code=<cities-municipalities_code>

                for each district
                take code
"""

__author__ = "seyLu"
__github__ = "github.com/seyLu"

__licence__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "seyLu"
__status__ = "Prototype"

import asyncio
import itertools
import logging
from logging.config import fileConfig

import aiohttp

REGION_VIII_CODE = "080000000"
CITY_OF_TACLOBAN_CODE = "083747000"

BASE_URL = "https://psgc.gitlab.io/api"
BASE_PATH = "results"

API_MAP = {
    "regions": "regions",
    "provinces": "provinces",
    "cities": "cities-municipalities",
    "districts": "barangays",
}

API_CHILD_MAP = {
    "regions": "provinces",
    "provinces": "cities",
    "cities": "districts",
    "districts": None,
}

API_PARENT_MAP = {
    "regions": None,
    "provinces": "regions",
    "cities": "provinces",
    "districts": "cities",
}


class PsgcAPI:
    def __init__(self, endpoint):
        self.base_endpoint: str = f"{BASE_URL}/{API_MAP[endpoint]}"
        self.child_endpoint: str | None = API_MAP.get(API_CHILD_MAP[endpoint])
        self.parent: str = API_PARENT_MAP[endpoint]
        self.model_name: str = f"regions.{endpoint}"
        self.items: list[dict] = []
        self.fixtures: list[dict] = []
        self.parent_child_codes: list[tuple[str, str]] = []

    async def list(
        self, session, parent_child_codes: list[tuple[str, str]] | None = None
    ):
        """Get all json items or select json items from api."""

        parent_codes: list[str] | None = None

        if not parent_child_codes:
            async with session.get(f"{self.base_endpoint}.json") as response:
                logging.info(f"Requesting {response.url}.")
                items = await response.json()
                codes = [item["code"] for item in items]
        else:
            parent_codes, codes = zip(*parent_child_codes)

        for pk, code in enumerate(codes, start=1):
            endpoint = f"{self.base_endpoint}/{code}"
            async with session.get(f"{endpoint}.json") as response:
                logging.info(f"Requesting {response.url}.")
                item = await response.json()

                fixture = {
                    "model": self.model_name,
                    "pk": pk,
                    "fields": {
                        "name": item["name"],
                        "code": item["code"],
                    },
                }

                if parent_codes:
                    if parent_code := parent_codes[pk - 1]:
                        fixture["fields"][f"{self.parent}_code"] = parent_code

                self.fixtures.append(fixture)

        return self.fixtures

    async def list_child_codes(self, session, code: str):
        """List child item codes."""

        endpoint = f"{self.base_endpoint}/{code}"
        child_endpoint = f"{endpoint}/{self.child_endpoint}"
        async with session.get(f"{child_endpoint}.json") as response:
            logging.info(f"Requesting {response.url}.")
            child_items = await response.json()

            self.parent_child_codes = list(
                zip(
                    itertools.repeat(code),
                    [child_item["code"] for child_item in child_items],
                )
            )

        return self.parent_child_codes


async def main():
    async with aiohttp.ClientSession() as session:
        regions_obj = PsgcAPI("regions")
        provinces_obj = PsgcAPI("provinces")
        cities_obj = PsgcAPI("cities")
        districts_obj = PsgcAPI("districts")

        region_fixtures = await regions_obj.list(session, [(None, REGION_VIII_CODE)])
        region_province_codes = [
            region_province_code
            for region_fixture in region_fixtures
            for region_province_code in await regions_obj.list_child_codes(
                session, region_fixture["fields"]["code"]
            )
        ]

        province_fixtures = await provinces_obj.list(session, region_province_codes)
        province_city_codes = [
            province_city_code
            for province_fixture in province_fixtures
            for province_city_code in await provinces_obj.list_child_codes(
                session, province_fixture["fields"]["code"]
            )
        ]

        city_fixtures = await cities_obj.list(session, province_city_codes)
        city_district_codes = [
            city_district_code
            for city_fixture in city_fixtures
            for city_district_code in await cities_obj.list_child_codes(
                session, city_fixture["fields"]["code"]
            )
        ]

        district_fixtures = await districts_obj.list(session, city_district_codes)

        print(f"{district_fixtures=}")


if __name__ == "__main__":
    fileConfig("logging.ini")
    asyncio.run(main())
