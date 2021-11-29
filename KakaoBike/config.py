import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

BASE_URL = os.getenv("BASE_URL")
X_AUTH_TOKEN = os.getenv("X_AUTH_TOKEN")
