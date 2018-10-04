from django import forms
from .models import Item, Transaction


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'value', 'quantity']


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['item', 'client']