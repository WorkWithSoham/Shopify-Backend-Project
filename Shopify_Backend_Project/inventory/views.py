from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status, views, request

from inventory.serializers import ItemSerializer
from inventory.models import Item


class ItemListAPIView(generics.ListAPIView):

    permission_classes = [permissions.AllowAny]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class ItemDetailAPIView(views.APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

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

    def delete(self, request, pk=None): 

        try:
            item = Item.objects.get(ItemID=pk)
        except Exception as e:
            return Response({
                'message': 'Item not found',
                'errors': str(e)
            },
                            status=status.HTTP_404_NOT_FOUND)

        item.delete()

        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk=None):

        data = request.data
        print(data)

        try:
            item = Item.objects.get(ItemID=pk)
        except Exception as e:
            return Response({
                'message': 'Item not found',
                'errors': str(e)
            },
                            status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemCreateAPIView(views.APIView):

    def post(self, request):

        data = request.data

        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



