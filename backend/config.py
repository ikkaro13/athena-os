import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    API_FOOTBALL_KEY = os.getenv("API_FOOTBALL_KEY", "")

    API_FOOTBALL_URL = "https://v3.football.api-sports.io"


settings = Settings()