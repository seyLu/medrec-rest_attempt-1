#!/usr/bin/env python

"""
1. retrieve from api (region, province, city, district)
2. create corresponding yaml fixtures

pseudocode:
get region viii
get all provinces with region_code=<region_code>
get all cities-municipalities with region_code=<region_code>
get all barangays with region_code=<region_code>
"""

__author__ = "seyLu"
__github__ = "github.com/seyLu"

__licence__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "seyLu"
__status__ = "Prototype"

import asyncio
import logging
import os
import shutil
from datetime import datetime
from logging.config import fileConfig

import aiohttp
import yaml

REGION_VIII_CODE: str = "080000000"
CITY_OF_TACLOBAN_CODE: str = "083747000"

BASE_URL: str = "https://psgc.gitlab.io/api"
BASE_PATH: str = "fixtures"

DATETIME_NOW: str = datetime.now().strftime("%Y%m%d%H%M%S")

API_MAP: dict = {
    "regions": "regions",
    "provinces": "provinces",
    "cities": "cities-municipalities",
    "districts": "barangays",
}

YAML_MAP: dict = {
    "regions": "Region",
    "provinces": "Province",
    "cities": "City",
    "districts": "District",
}


class PsgcAPI:
    def __init__(self, endpoint: str):
        self.url: str = self._get_url(endpoint)
        self.model_name: str = YAML_MAP[endpoint].lower()
        self.yaml_filename: str = os.path.join(BASE_PATH, f"{YAML_MAP[endpoint]}.yaml")

    def __str__(self):
        return f"PsgcAPI(\n  url={self.url},\n  model_name={self.model_name},\n  yaml_filename={self.yaml_filename}\n)\n"

    def _get_url(self, endpoint: str) -> str:
        url: str = BASE_URL
        region_url: str = f"{url}/regions/{REGION_VIII_CODE}"

        if endpoint != "regions":
            url = f"{region_url}/{API_MAP[endpoint]}"
        else:
            url = region_url

        return f"{url}.json"

    async def _get_json(self, session) -> list[dict]:
        logging.info(f"Requesting {self.url}")
        async with session.get(self.url) as response:
            if response.content_type != "application/json":
                raise ValueError(f"Unexpected content type: {response.content_type}")
            return await response.json()

    async def _get_fixtures(self, session) -> list[dict]:
        items: list[dict] = await self._get_json(session)
        if not isinstance(items, list):
            items = [items]

        logging.info(f"Serializing fixture {self.model_name}")
        return [
            await self._get_fixture(item, pk) for pk, item in enumerate(items, start=1)
        ]

    async def _get_fixture(self, item: dict, pk: int) -> dict:
        fixture: dict = {
            "model": f"regions.{self.model_name}",
            "pk": pk,
            "fields": {
                "code": item["code"],
                "name": item["name"],
            },
        }

        if self.model_name != "region":
            fixture["fields"]["region_code"] = item["regionCode"]

            if self.model_name != "province":
                fixture["fields"]["province_code"] = item["provinceCode"]

                if self.model_name != "city":
                    if city_code := item.get("municipalityCode"):
                        fixture["fields"]["city_code"] = city_code
                    else:
                        fixture["fields"]["city_code"] = item["cityCode"]

        return fixture

    async def _get_yaml(self, session):
        logging.info(f"Generating {self.yaml_filename}")
        return yaml.dump(
            await self._get_fixtures(session), default_flow_style=False, sort_keys=False
        )

    def _backup_yaml(self) -> None:
        logging.info(f"Generating backup {self.yaml_filename}.bak")
        dest: str = os.path.join(
            "results", DATETIME_NOW, f"{self.yaml_filename.split('/')[-1]}.bak"
        )
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(self.yaml_filename, dest)

    async def generate_fixture(self, session) -> None:
        if os.path.isfile(self.yaml_filename):
            self._backup_yaml()

        with open(self.yaml_filename, "w+") as f:
            print(await self._get_yaml(session), file=f)


async def main():
    async with aiohttp.ClientSession() as session:
        endpoints: list[str] = [
            "regions",
            "provinces",
            "cities",
            "districts",
        ]

        for endpoint in endpoints:
            await PsgcAPI(endpoint).generate_fixture(session)


if __name__ == "__main__":
    fileConfig("logging.ini")
    asyncio.run(main())
    logging.info("Succesfully generated regions fixture")
