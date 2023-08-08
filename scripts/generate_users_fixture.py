#!/usr/bin/env python

"""
Using OPENAI

generate users fixture based on specified fields
"""

__author__ = "seyLu"
__github__ = "github.com/seyLu"

__licence__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "seyLu"
__status__ = "Prototype"


from logging.config import fileConfig

import phonenumbers
import yaml
from faker import Faker


def main():
    fake = Faker(["en_PH"])
    Faker.seed(0)

    fixtures: list[dict] = []
    for pk in range(1, 101):
        is_email_verified = fake.boolean(chance_of_getting_true=75)
        fixtures.append(
            {
                "model": "models.user",
                "pk": pk,
                "fields": {
                    "first_name": fake.first_name(),
                    "last_name": fake.last_name(),
                    "email": fake.ascii_safe_email(),
                    "mobile_number": phonenumbers.format_number(
                        phonenumbers.parse(fake.mobile_number(), "PH"),
                        phonenumbers.PhoneNumberFormat.E164,
                    ),
                    "is_email_verified": is_email_verified,
                    "is_mobile_verified": fake.boolean(chance_of_getting_true=75),
                    "is_active": is_email_verified,
                    "is_staff": True if pk == 1 else False,
                },
            }
        )

    with open("results/User.yaml", "w+") as f:
        print(
            yaml.dump(
                fixtures,
                default_flow_style=False,
                sort_keys=False,
            ),
            file=f,
        )


if __name__ == "__main__":
    fileConfig("logging.ini")
    main()
