# todo_api/tests/factories.py

import factory
from portfolio_management.models.auth import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    # Add other fields as needed
