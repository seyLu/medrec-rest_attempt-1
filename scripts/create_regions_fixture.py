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
import json

import requests

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

FIXTURE_JSON_MAP = {
    "model": None,
    "pk": None,
    "fields": {
        "name": None,
        "code": None,
    },
}


async def main():
    regions, province_codes = await get_regions()
    # provinces, city_codes = get_provinces(province_codes)
    # cities, district_codes = get_cities(city_codes)
    # districts = get_districts(district_codes)

    print(f"{regions=}\n{province_codes=}")


async def get_regions(codes: list[str] | None = None) -> tuple:
    """Get all regions or select regions from api."""

    regions: list[dict]
    fixtures: list[dict] = []
    province_codes: list[str] = []

    MODEL_NAME: str = "regions.region"
    BASE_ENDPOINT: str = f"{BASE_URL}/regions"

    if not codes:
        regions = requests.get(BASE_ENDPOINT).json()
        codes = [region["code"] for region in regions]

    for pk, code in enumerate(codes, start=1):
        fixture, province_code_list = await get_region(
            BASE_ENDPOINT=BASE_ENDPOINT, MODEL_NAME=MODEL_NAME, code=code, pk=pk
        )

        fixtures.append(fixture)
        province_codes.extend(province_code_list)

    return fixtures, province_codes


async def get_region(BASE_ENDPOINT, MODEL_NAME, code, pk):
    """Get a single region from api."""

    endpoint = f"{BASE_ENDPOINT}/{code}"
    region = requests.get(endpoint).json()

    fixture = {
        "model": MODEL_NAME,
        "pk": pk,
        "fields": {
            "name": region["name"],
            "code": region["code"],
        },
    }

    provinces_endpoint = f"{endpoint}/provinces"
    provinces = requests.get(provinces_endpoint).json()
    province_code_list = [province["code"] for province in provinces]

    return fixture, province_code_list


def _() -> None:
    """@TODO."""

    province_set = city_set = district_set = set()

    region_endpoint = f"{BASE_URL}/regions/{REGION_VIII_CODE}"
    region_res = requests.get(region_endpoint)

    provinces_endpoint = f"{region_endpoint}/provinces"
    provinces_json = requests.get(provinces_endpoint).json()

    for province in provinces_json:
        province_endpoint = f"{BASE_URL}/provinces/{province['code']}"
        province_res = requests.get(province_endpoint)
        province_set.add(province_res)

        cities_endpoint = f"{province_endpoint}/cities-municipalities"
        cities_json = requests.get(cities_endpoint).json()

        for city in cities_json:
            city_endpoint = f"{BASE_URL}/cities-municipalities/{city['code']}"
            city_res = requests.get(city_endpoint)
            city_set.add(city_res)

            districts_endpoint = f"{city_endpoint}/barangays"
            districts_json = requests.get(districts_endpoint).json()

            for district in districts_json:
                district_endpoint = f"{BASE_URL}/barangays/{district['code']}"
                district_res = requests.get(district_endpoint)
                district_set.add(district_res)

    city_of_tacloban_endpoint = f"{BASE_URL}/cities/{CITY_OF_TACLOBAN_CODE}"
    city_of_tacloban_res = requests.get(city_of_tacloban_endpoint)
    city_set.add(city_of_tacloban_res)

    city_of_tacloban_districts_endpoint = f"{city_of_tacloban_endpoint}/barangays"
    city_of_tacloban_districts_json = requests.get(
        city_of_tacloban_districts_endpoint
    ).json()

    for district in city_of_tacloban_districts_json:
        district_endpoint = f"{BASE_URL}/barangays/{district['code']}"
        district_res = requests.get(district_endpoint)
        district_set.add(district_res)

    with open(f"{BASE_PATH}/regions.txt", "w+") as f:
        f.write(json.dumps(region_res.json(), indent=2))

    with open(f"{BASE_PATH}/provinces.txt", "w+") as f:
        for province in province_set:
            f.write(json.dumps(province.json(), indent=2))

    with open(f"{BASE_PATH}/cities.txt", "w+") as f:
        for city in city_set:
            f.write(json.dumps(city.json(), indent=2))

    with open(f"{BASE_PATH}/districts.txt", "w+") as f:
        for district in district_set:
            f.write(json.dumps(district.json(), indent=2))


if __name__ == "__main__":
    asyncio.run(main())
