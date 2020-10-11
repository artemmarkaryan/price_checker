import dotenv
import os

dotenv.load_dotenv()

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'accept': '*/*'
}

PRICE_SIMILARITY_RATIO = 0.7

DB_PASSWORD = os.getenv('DB_PASSWORD')

BOT_TOKEN = os.getenv('BOT_TOKEN')

# WEBHOOK_HOST = '5.63.155.152'
# WEBHOOK_PORT = 80
# WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше
#
# WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Путь к сертификату
# WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Путь к приватному ключу
#
# WEBHOOK_URL_BASE = f"https://{WEBHOOK_HOST}:{WEBHOOK_PORT}"
# WEBHOOK_URL_PATH = f"/{BOT_TOKEN}/"
