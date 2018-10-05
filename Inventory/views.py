from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, Transaction, Client, Value, Category
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import ItemForm
from django import forms


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'items_list'

    def get_queryset(self):
        return Item.objects.all()


class ItemCreate(generic.CreateView):
    model = Item
    fields = ['name', 'category', 'value', 'quantity']


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('Inventory:index')


class ClientCreate(generic.CreateView):
    model = Client
    fields = ['place', 'description']


class CategoryCreate(generic.CreateView):
    model = Category
    fields = ['category']


class ValueCreate(generic.CreateView):
    model = Value
    fields = ['value']


class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('Inventory:index')


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('Inventory:index')


class ValueDelete(DeleteView):
    model = Value
    success_url = reverse_lazy('Inventory:index')




def details(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    clients = Client.objects.all()
    value = Value.objects.all()
    return render(request, 'details.html', {'item': item, 'clients': clients, 'value': value})


def transferitm(request, item_id):
    client = Client.objects.get(place=request.POST.get("client"))
    value = request.POST.get("value")
    item = Item.objects.get(pk=item_id)
    quantity = request.POST.get("quantity")
    transaction = Transaction(quantity=quantity, item=item, client=client)
    transaction.save()
    item.quantity = item.quantity - int(quantity)
    item.save()
    return render(request, 'transferitm.html',
                  {'transaction': transaction, 'quantity': quantity, 'item': item, 'client': client})


def returnitm(request, item_id):
    client = Client.objects.get(place=request.POST.get("client"))
    value = request.POST.get("value")
    item = Item.objects.get(pk=item_id)
    quantity = request.POST.get("quantity")
    transaction = Transaction(quantity=quantity, item=item, client=client)
    transaction.save()
    if item.value is not value:
        item.quantity = item.quantity
    else:
        item.quantity = item.quantity + int(quantity)
        item.save()
    return render(request, 'returnitm.html',
                  {'transaction': transaction, 'quantity': quantity, 'item': item, 'client': client})




