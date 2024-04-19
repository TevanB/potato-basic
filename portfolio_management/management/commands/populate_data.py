import random

from django.db import transaction
from django.core.management.base import BaseCommand

from portfolio_management.models.auth import User
from portfolio_management.models.holdings import HoldingItem, Portfolio
from .utils.factories import (
    UserFactory,
    HoldingItemFactory,
    PortfolioFactory,
)

NUM_USERS = 10
NUM_PORTFOLIOS = 10
NUM_HOLDINGS = 5
USERS_PER_PORTFOLIO = 2


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [User, HoldingItem, Portfolio]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        # Create all the users
        people = UserFactory.create_batch(NUM_USERS)

        portfolios = PortfolioFactory.create_batch(NUM_PORTFOLIOS)

        for portfolio in portfolios:
            holdings = HoldingItemFactory.create_batch(
                NUM_HOLDINGS, portfolio=portfolio
            )
            portfolio.holding_list.set(holdings)

        for user in people:
            choices = random.choices(portfolios, k=USERS_PER_PORTFOLIO)
            user.holdings.add(*choices)
