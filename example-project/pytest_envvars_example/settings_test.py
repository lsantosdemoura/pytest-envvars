from .settings import *


class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'TEST-NAME': ':memory:',
    }
}


TEST_CUSTOMER_NAME = config('TEST_CUSTOMER_NAME')
TEST_CUSTOMER_EMAIL = config('TEST_CUSTOMER_EMAIL')
TEST_PRODUCT_ID = config('TEST_PRODUCT_ID')
