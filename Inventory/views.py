from django.shortcuts import render, render_to_response

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, Transaction, Client, Value, Category
from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404
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


# def index(request):
#    items_list = Item.objects.all()
#    context = {
#        'items_list': items_list,
#    }
#    return render(request, 'index.html', context)


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

    # class ItemCreate(CreateView):
    #    model = Item
    #    fields = ['name', 'category', 'value', 'quantity']


