from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=20)
    store = models.ForeignKey("Store", on_delete=models.CASCADE)



class Store(models.Model):
    store_name = models.CharField(max_length=20)

    def length_name(self):
        if len(self.store_name) > 10:
            return len(self.store_name)
        else:
            return 0

class ShopList(models.Model):
    shoplist_name = models.CharField(max_length=20)
    items = models.ManyToManyField(Item, through="ItemShopList", through_fields=("shop_list", "item"))

    def __str__(self):
        return self.shoplist_name



class ItemShopList(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    shop_list = models.ForeignKey(ShopList, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    already_bought = models.BooleanField()