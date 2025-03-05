from .common import *

DEBUG = True

SECRET_KEY = "django-insecure-w#4km0_po#)#^uq%de514vay3nd$&mth1td8^x=_p@t+f4b0e)"

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE"),
        "NAME": os.getenv("DB_NAME"),
        "HOST": os.getenv("DB_HOST"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
    }
}
