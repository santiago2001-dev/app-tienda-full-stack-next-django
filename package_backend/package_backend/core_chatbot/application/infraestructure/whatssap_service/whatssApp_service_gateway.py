
import requests


class ExternalGateway:
    def __init__(self, base_url):
        self.base_url = base_url

    def send_post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
