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

import requests
import json

REGION_VIII_CODE = "080000000"
CITY_OF_TACLOBAN_CODE = "0831600000"

base_url = "https://psgc.gitlab.io/api"
base_path = "results"

province_set = city_set = district_set = set()

region_endpoint = f"{base_url}/regions/{REGION_VIII_CODE}"
region_res = requests.get(region_endpoint)

provinces_endpoint = f"{region_endpoint}/provinces"
provinces_json = requests.get(provinces_endpoint).json()

for province in provinces_json:
    province_endpoint = f"{base_url}/provinces/{province['code']}"
    province_res = requests.get(province_endpoint)
    province_set.add(province_res)

    cities_endpoint = f"{province_endpoint}/cities-municipalities"
    cities_json = requests.get(cities_endpoint).json()

    for city in cities_json:
        city_endpoint = f"{base_url}/cities-municipalities/{city['code']}"
        city_res = requests.get(city_endpoint)
        city_set.add(city_res)

        districts_endpoint = f"{city_endpoint}/barangays"
        districts_json = requests.get(districts_endpoint).json()

        for district in districts_json:
            district_endpoint = f"{base_url}/barangays/{district['code']}"
            district_res = requests.get(district_endpoint)
            district_set.add(district_res)


city_of_tacloban_endpoint = f"{base_url}/cities/{CITY_OF_TACLOBAN_CODE}"
city_of_tacloban_res = requests.get(city_of_tacloban_endpoint)
city_set.add(city_of_tacloban_res)

city_of_tacloban_districts_endpoint = f"{city_of_tacloban_endpoint}/barangays"
city_of_tacloban_districts_json = requests.get(city_of_tacloban_districts_endpoint).json()

for district in city_of_tacloban_districts_json:
    district_endpoint = f"{base_url}/barangays/{district['code']}"
    district_res = requests.get(district_endpoint)
    district_set.add(district_res)


with open(f"{base_path}/regions.txt", "w+") as f:
    f.write(json.dumps(region_res.json(), indent=2))

with open(f"{base_path}/provinces.txt", "w+") as f:
    for province in province_set:
        f.write(json.dumps(province.json(), indent=2))

with open(f"{base_path}/cities.txt", "w+") as f:
    for city in city_set:
        f.write(json.dumps(city.json(), indent=2))

with open(f"{base_path}/districts.txt", "w+") as f:
    for district in district_set:
        f.write(json.dumps(district.json(), indent=2))
