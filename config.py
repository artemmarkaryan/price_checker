import dotenv
import os

dotenv.load_dotenv()

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',

}

PRICE_SIMILARITY_RATIO = 0.7

DB_PASSWORD = os.getenv('DB_PASSWORD')

BOT_TOKEN = os.getenv('BOT_TOKEN')


class KbButtons:
    CANCEL = 'Отмена'
    ADD = '➕ Новая ссылка'


# WEBHOOK_HOST = '5.63.155.152'
# WEBHOOK_PORT = 80
# WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше
#
# WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Путь к сертификату
# WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Путь к приватному ключу
#
# WEBHOOK_URL_BASE = f"https://{WEBHOOK_HOST}:{WEBHOOK_PORT}"
# WEBHOOK_URL_PATH = f"/{BOT_TOKEN}/"
