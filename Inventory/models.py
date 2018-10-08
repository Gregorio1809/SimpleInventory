from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('Inventory:index')

    def __str__(self):
        return self.category


class Value(models.Model):
    value = models.CharField(max_length=20, default='Kilograms')

    def get_absolute_url(self):
        return reverse('Inventory:index')

    def __str__(self):
        return self.value


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat')
    value = models.ForeignKey(Value, on_delete=models.CASCADE, blank=True, null=True, related_name='val')
    quantity = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('Inventory:details', kwargs={'item_id': self.item_id})


def __str__(self):
    return self.name


class Client(models.Model):
    place = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('Inventory:index')

    def __str__(self):
        return ("%s, %s" % (self.place, self.description))


class Transaction(models.Model):
    trans_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    time = models.DateTimeField(auto_now=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return ("%s , %s , %s" % (self.item.name, self.client.place, self.time))
