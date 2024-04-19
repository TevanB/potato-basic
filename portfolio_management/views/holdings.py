from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from portfolio_management.models.auth import User
from portfolio_management.models.holdings import Portfolio
from portfolio_management.serializers import UserSerializer, PortfolioSerializer


class HoldingListView(APIView):
    """
    View to retrieve holdings from a user
    """

    def get(self, request, pk):
        try:
            portfolio = User.objects.get(id=pk).holdings.all()[0]
            serializer_context = {
                "request": request,
            }
            portfolio_serialized = PortfolioSerializer(
                portfolio, context=serializer_context
            )
            return Response(portfolio_serialized.data)
        except Portfolio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
