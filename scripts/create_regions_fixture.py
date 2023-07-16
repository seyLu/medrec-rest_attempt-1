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

import json
import os

import requests

REGION_VIII_CODE = "080000000"
CITY_OF_TACLOBAN_CODE = "0831600000"

BASE_URL = "https://psgc.gitlab.io/api"
BASE_PATH = "results"


def main():
    _()


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
    main()
