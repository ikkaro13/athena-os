import requests


class HttpClient:
    """Cliente HTTP reutilizable para Athena."""

    def get(self, url, headers=None, params=None):
        try:
            response = requests.get(
                url=url,
                headers=headers,
                params=params,
                timeout=30,
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException as e:
            print(f"[HTTP ERROR] {e}")
            return None