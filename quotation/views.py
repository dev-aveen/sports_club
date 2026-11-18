from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Quote
from .serializers import QuoteSerializer


class AdminQuoteListCreateAPIView(ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUser]


class AdminQuoteDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUser]

 
    def patch(self, request, *args, **kwargs):
        Quote.objects.update(is_featured=False)
        quote = self.get_object()
        quote.is_featured = True
        quote.save()
        serializer = self.get_serializer(quote)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FeaturedQuoteAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        quote = Quote.objects.filter(is_featured=True).first()
        if not quote:
            return Response(
                {"detail": "No featured maxim found."},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(QuoteSerializer(quote).data)