from portfolio_management.models.holdings import HoldingItem, Portfolio
from portfolio_management.models.auth import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "portfolio"]


class HoldingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoldingItem
        fields = "__all__"  # Include all fields from the Holding model

    def to_representation(self, instance):
        return super().to_representation(instance)


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"

    def to_representation(self, instance):
        return super().to_representation(instance)
