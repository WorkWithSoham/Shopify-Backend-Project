from django.urls import path
from inventory.views import *

urlpatterns = [
    path('', ItemListAPIView.as_view(), name='ItemList'),
    path('<int:pk>', ItemDetailAPIView.as_view(), name='ItemDetails'),
    path('create/', ItemCreateAPIView.as_view(), name='CreateItem'),
    path('csv/', ProduceCSV.as_view(), name='ProductCSV')
]