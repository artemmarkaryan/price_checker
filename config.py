import dotenv
import os

dotenv.load_dotenv()

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'accept': '*/*'
}

PRICE_SIMILARITY_RATIO = 0.7

DB_PASSWORD = os.getenv('DB_PASSWORD')