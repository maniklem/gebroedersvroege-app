import requests, json


class MoneyBird:

    version = "v2"
    administration_id = "217115833077335589"
    base_url = f"https://moneybird.com/api/{version}/{administration_id}"

    @classmethod
    def get_auth_header(cls):
        return {"Authorization": "Bearer 8S4N-aIMRAHJjxazp_QfB9dw0qUJtDy-WikkkXvLA_c"}

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


loonwerk_klanten = MoneyBird.get_all_loonwerk_klanten()
