import requests, json, os
from pprint import pprint

class MoneyBird:

    version = os.getenv("MONEYBIRD_VERSION", "v2")
    administration_id = os.getenv("MONEYBIRD_ADMINISTRATION_ID")
    bearer_token = os.getenv("MONEYBIRD_BEARER_TOKEN")

    base_url = f"https://moneybird.com/api/{version}/{administration_id}"

    @classmethod
    def get_auth_header(cls):
        return {"Authorization": f"Bearer {cls.bearer_token}"}

    @classmethod
    def get_all_loonwerk_klanten(cls):
        loonwerk_klanten = []
        page = 0
        while True:
            page += 1
            response = requests.get(
                url=cls.base_url + f"/contacts.json?page={page}",
                headers=cls.get_auth_header(),
            )
            if response.json() == []:
                break
            loonwerk_klanten.append(
                [
                    x
                    for x in response.json()
                    if list(
                        filter(
                            lambda custom_field: custom_field["value"] == "loonwerk"
                            and custom_field["name"] == "soort_klant",
                            x["custom_fields"],
                        )
                    )
                ]
            )
        return [item for sublist in loonwerk_klanten for item in sublist]

    @classmethod
    def get_products_based_on_categories(cls, categorie:str):
        producten = []
        page = 0
        while True:
            page += 1
            response = requests.get(
                url=cls.base_url + f"/products.json?page={page}",
                headers=cls.get_auth_header(),
            )
            if response.json() == []:
                
                break
            for x in response.json():
                pprint(x["category"])
        #     producten.append(
        #         [
        #             x
        #             for x in response.json()
        #             if list(
        #                 filter(
        #                     lambda custom_field: custom_field["value"] == "loonwerk"
        #                     and custom_field["name"] == "soort_klant",
        #                     x["custom_fields"],
        #                 )
        #             )
        #         ]
        #     )
        # return [item for sublist in producten for item in sublist]

    @classmethod
    def get_product_based_on_identifier(cls, identifier:str):
        response = requests.get(
            url=cls.base_url + f"/products/{identifier}",
            headers=cls.get_auth_header(),
        )
        pprint(response.json())

    @classmethod
    def get_custom_fields(cls):
        response = requests.get(
            url=cls.base_url + f"/custom_fields",
            headers=cls.get_auth_header(),
        )
        pprint(response.json())

products = MoneyBird.get_custom_fields()
