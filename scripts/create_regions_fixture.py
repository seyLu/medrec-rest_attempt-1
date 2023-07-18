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
import yaml
import os
from logging.config import fileConfig

import aiohttp

import json

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

SAMPLE_FIXTURE_MAP = [
    {
        "model": "regions.province",
        "pk": "1",
        "fields": {
            "region_code": "0800000000",
            "name": "City of Tacloban",
            "code": "0831600000",
        },
    }
]


async def main():
    async with aiohttp.ClientSession() as session:
        region_viii_regions_url: str = await get_api_map(
            BASE_URL, f"regions/{REGION_VIII_CODE}"
        )
        region_viii_provinces_url: str = await get_api_map(
            region_viii_regions_url, "provinces"
        )
        region_viii_cities_url: str = await get_api_map(
            region_viii_regions_url, "cities"
        )
        region_viii_districts_url: str = await get_api_map(
            region_viii_regions_url, "districts"
        )

        region_viii_regions_json: dict = await get_json_response(session, f"{region_viii_regions_url}.json")
        region_viii_provinces_json: dict = await get_json_response(session, region_viii_provinces_url)
        region_viii_cities_json: dict = await get_json_response(session, region_viii_cities_url)
        region_viii_districts_json: dict = await get_json_response(session, region_viii_districts_url)

        region_fixtures: dict = await get_fixtures("region", region_viii_regions_json)
        province_fixtures: dict = await get_fixtures("province", region_viii_provinces_json)
        city_fixtures: dict = await get_fixtures("city", region_viii_cities_json)
        district_fixtures: dict = await get_fixtures("district", region_viii_districts_json)

        with open(
            os.path.join(BASE_PATH, "Region.yaml"), "w+"
        ) as f:
            print(get_yaml(region_fixtures), file=f)

        with open(
            os.path.join(BASE_PATH, "Province.yaml"), "w+"
        ) as f:
            print(get_yaml(province_fixtures), file=f)

        with open(
            os.path.join(BASE_PATH, "City.yaml"), "w+"
        ) as f:
            print(get_yaml(city_fixtures), file=f)

        with open(
            os.path.join(BASE_PATH, "District.yaml"), "w+"
        ) as f:
            print(get_yaml(district_fixtures), file=f)



async def get_api_map(url: str, endpoint: str) -> str:
    if api_endpoint := API_MAP.get(endpoint):
        url += f"/{api_endpoint}.json"
    else:
        url += f"/{endpoint}"

    return f"{url}"


async def get_json_response(session, url: str):
    async with session.get(url) as response:
        if response.content_type != "application/json":
            raise ValueError(f"Unexpected content type: {response.content_type}")

        return await response.json()


async def get_fixtures(name: str, items: list[dict]) -> list[dict]:
    if not isinstance(items, list):
        items = [items]
    return [await get_fixture(name, item, pk) for pk, item in enumerate(items, start=1)]


async def get_fixture(name: str, item: dict, pk) -> dict:
    fixture: dict = {
        "model": f"regions.{name}",
        "pk": pk,
        "fields": {
            "code": item["code"],
            "name": item["name"],
        }
    }

    if name != "region":
        fixture["fields"]["region_code"] = item["regionCode"]

        if name != "province":
            fixture["fields"]["province_code"] = item["provinceCode"]

            if name != "city":
                if city_code := item.get("municipalityCode"):
                    fixture["fields"]["city_code"] = city_code
                fixture["fields"]["city_code"] = item["cityCode"]

    return fixture


def get_yaml(fixture: dict):
    return yaml.dump(fixture, default_flow_style=False, sort_keys=False)


if __name__ == "__main__":
    fileConfig("logging.ini")
    asyncio.run(main())
