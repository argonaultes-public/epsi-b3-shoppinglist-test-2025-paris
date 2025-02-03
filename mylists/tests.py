from django.test import TestCase
from django.db.utils import IntegrityError

from .models import Item, Store
# Create your tests here.

class StoreItemTest(TestCase):


    def test_create_item(self):
        store = Store.objects.create(store_name='marche')
        Item.objects.create(item_name='orange', store=store)
        item_from_db = Item.objects.get(item_name='orange')
        self.assertIsNotNone(item_from_db)
        self.assertEquals(item_from_db.item_name, 'orange')

    def test_create_item_error(self):
        with self.assertRaises(IntegrityError):
            Item.objects.create(item_name='orange')

    def test_create_store_too_long_names(self):
        with self.assertRaises(IntegrityError):
            Store.objects.create(store_name='a'*100)