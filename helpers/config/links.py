import os

from dotenv import load_dotenv

load_dotenv()


class Links:

    BASE_URL = os.getenv('BASE_URL')
