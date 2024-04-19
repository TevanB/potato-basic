import factory
from portfolio_management.models.auth import User
from portfolio_management.models.holdings import HoldingItem, Portfolio


class HoldingItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HoldingItem

    symbol = factory.Faker("word")
    company_name = factory.Faker("company")
    quantity_held = factory.Faker("pyint", min_value=1, max_value=100)
    purchase_price = factory.Faker(
        "pydecimal", left_digits=5, right_digits=2, positive=True
    )
    purchase_date = factory.Faker("date_this_decade")
    current_price = factory.Faker(
        "pydecimal", left_digits=5, right_digits=2, positive=True
    )
    total_value = factory.Faker(
        "pydecimal", left_digits=7, right_digits=2, positive=True
    )
    currency = factory.Faker("currency_code")
    notes = factory.Faker("text")
    sector = factory.Faker("word")
    dividends_received = factory.Faker(
        "pydecimal", left_digits=5, right_digits=2, positive=True
    )


class PortfolioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Portfolio


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.Faker("password")
