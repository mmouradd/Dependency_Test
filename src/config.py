"""
Loads configuration from a .env file (if present) with sane defaults.
"""

import os
from dotenv import load_dotenv

load_dotenv()

API_TIMEOUT = int(os.getenv("API_TIMEOUT", "5"))
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data.db")
