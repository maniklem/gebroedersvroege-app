import requests


class MoneyBird:

    version = "v2"
    administration_id = "217115833077335589"
    base_url = f"https://moneybird.com/api/{version}/{administration_id}"

    @classmethod
    def get_auth_header(cls):
        return {"Authorization": "Bearer 8S4N-aIMRAHJjxazp_QfB9dw0qUJtDy-WikkkXvLA_c"}

    @classmethod
    def get_all_loonwerk_klanten(cls):
        response = requests.get(
            url=cls.base_url + "/contacts", headers=cls.get_auth_header()
        )
        return response.json()


print(MoneyBird.get_all_loonwerk_klanten())
