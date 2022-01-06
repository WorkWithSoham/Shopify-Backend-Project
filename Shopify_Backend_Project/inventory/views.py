from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status, views, request

from inventory.serializers import ItemSerializer
from inventory.models import Item


class ItemListAPIView(generics.ListAPIView):

    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDetailAPIView(views.APIView):

    def get(self, request, pk=None):

        try:
            data = Item.objects.get(ItemID=pk)
        except Exception as e:
            return Response({
                'message': 'Item not found',
                'errors': str(e)
            },
            status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(data)

        return Response(serializer.data)

    def post(self, request):

        try:
            data = Item.objects.get(ItemID=pk)
        except Exception as e:
            return Response({
                'message': 'Item not found',
                'errors': str(e)
            },
            status=status.HTTP_404_NOT_FOUND)

        data = request.data

        return Response({data}, status=status.HTTP_200_OK)
        


