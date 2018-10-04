from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'Inventory'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<item_id>[0-9]+)/detail/$', views.details, name='details'),
    # url(r'^(?P<item_id>[0-9]+)/detail/transfer/$', views.returnitm, name='transferitm'),
    # url(r'^(?P<item_id>[0-9]+)/detail/return/$', views.returnitm(), name='returnitm'),
    url(r'^item/add/$', views.CreateView.as_view(), name='create'),

    # path('', views.index, name='index'),
    # path('<int:item_id>/', views.details, name='details'),
    # path('create', views.CreateView.as_view(), name='album_add'),
    path('<int:item_id>/detail/transfer', views.transferitm, name='transferitm'),
    path('<int:item_id>/detail/return', views.returnitm, name='returnitm'),
]
