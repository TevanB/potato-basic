import json
from django.db import models
from .auth import User


class HoldingItem(models.Model):
    symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    quantity_held = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3)
    portfolio = models.ForeignKey("Portfolio", on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    sector = models.CharField(max_length=50, blank=True)
    dividends_received = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        return f"{self.company_name} ({self.symbol})"


class Portfolio(models.Model):
    holding_list = models.ManyToManyField(HoldingItem, related_name="+")

    def __str__(self):
        return f"Portfolio with {len(self.holding_list.all())} holdings."
