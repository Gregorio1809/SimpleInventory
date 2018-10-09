from django.shortcuts import render, render_to_response

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateResponseMixin
from django.template import RequestContext

from .models import Item, Transaction, Client, Value, Category
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .forms import ItemForm, ClientForm, CategoryForm, ValueForm


class IndexView(generic.ListView):
    template_name = 'items.html'
    context_object_name = 'items_list'

    def get_queryset(self):
        return Item.objects.all()


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class ItemCreate(generic.CreateView):
    model = Item
    fields = ['name', 'category', 'value', 'quantity']


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('Inventory:index')


class ClientCreate(generic.CreateView, generic.ListView, TemplateResponseMixin):
    model = Client
    form_class = ClientForm
    template_name = 'Inventory/client_form.html'
    context_object_name = 'client_list'

    def get_queryset(self):
        return Client.objects.all()


class CategoryCreate(generic.CreateView, generic.ListView, TemplateResponseMixin):
    model = Category
    form_class = CategoryForm
    template_name = 'Inventory/category_form.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.all()


class ValueCreate(generic.CreateView, generic.ListView, TemplateResponseMixin):
    model = Value
    form_class = ValueForm
    template_name = 'Inventory/value_form.html'
    context_object_name = 'value_list'

    def get_queryset(self):
        return Value.objects.all()


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
    value = Item.objects.filter(pk=item_id)
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


def handler404(request, *args, **kwargs):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **kwargs):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response
