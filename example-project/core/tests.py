import pytest
from django.conf import settings

from core.models import Customer
from core.models import FavoriteList


@pytest.mark.django_db(transaction=True)
class TestModelsSetUp:
    @pytest.fixture
    def customer_name(self):
        name = 'Random Customer Name'
        return name

    @pytest.fixture
    def customer_email(self):
        email = "email@email.com"
        return email

    @pytest.fixture
    def test_customer(self, customer_name, customer_email):
        test_customer = Customer.objects.create(
            name=customer_name,
            email=customer_email,
        )
        return test_customer

    @pytest.fixture
    def product_id(self):
        product_id = settings.TEST_PRODUCT_ID
        return product_id

    @pytest.fixture
    def test_favorite_list(self, test_customer, product_id):
        test_favorite_list = FavoriteList.objects.create(
            customer=test_customer,
            product_id=product_id,
        )
        return test_favorite_list


@pytest.mark.django_db(transaction=True)
class TestCustomers(TestModelsSetUp):

    def test_customer_instance(self, test_customer):
        assert isinstance(test_customer, Customer)

    def test_customer_get_name(self, test_customer, customer_name):
        assert test_customer.name == customer_name

    def test_customer_get_email(self, test_customer, customer_email):
        assert test_customer.email == customer_email

    def test_customer_str(self, test_customer, customer_name):
        assert test_customer.__str__() == customer_name

    def test_get_wrong_name(self, test_customer):
        """Checks if the customer name is being changed with pytest envvars."""
        assert test_customer.name != settings.TEST_CUSTOMER_NAME

    def test_get_wrong_email(self, test_customer):
        """Checks if the customer email is being changed with pytest envvars."""
        assert test_customer.email != settings.TEST_CUSTOMER_EMAIL


@pytest.mark.django_db(transaction=True)
class TestFavoriteList(TestModelsSetUp):

    def test_product_instance(self, test_favorite_list):
        assert isinstance(test_favorite_list, FavoriteList)

    def test_product_str(self, test_favorite_list, product_id):
        assert test_favorite_list.__str__() == product_id
