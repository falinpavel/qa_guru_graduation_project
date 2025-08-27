import os

from dotenv import load_dotenv

load_dotenv()


class Links:

    BASE_URL = os.getenv('BASE_URL')

    DODO_CONTROL_URL = os.getenv('DODO_CONTROL_URL')

    ABOUT_US_PAGE_URL = '/about'

    CONTACTS_PAGE_URL = '/contacts'

    CORPORATE_ORDERS_PAGE_URL = '/b2b'

    GIFT_CERTIFICATES_PAGE_URL = f'{BASE_URL}/certificates'
