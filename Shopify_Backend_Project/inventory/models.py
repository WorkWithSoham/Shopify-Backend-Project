from django.db import models


class Item(models.Model):

    ItemID = models.AutoField(primary_key=True)
    ItemName = models.CharField(max_length=30, null=False)
    ItemDescription = models.TextField(null=True, blank=True)
    ItemPrice = models.IntegerField(default=0)
    ItemQuantity = models.IntegerField(default=0)

    # def __str__(self):
    #     return str(self.ItemID) + '_' + self.ItemName
