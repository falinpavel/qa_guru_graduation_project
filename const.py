import os.path


class Const:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    RESOURCES_DIR = os.path.join(BASE_DIR, 'resources')

    DEFAULT_BROWSER_VERSION = "128.0"

    DEFAULT_BROWSER_TYPE = "chrome"
