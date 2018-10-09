from django import forms
from .models import Item, Transaction, Client, Category, Value


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'value', 'quantity']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['item', 'client']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['place', 'description']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']


class ValueForm(forms.ModelForm):
    class Meta:
        model = Value
        fields = ['value']
