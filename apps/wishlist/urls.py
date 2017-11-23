from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name="main"),
    url(r'^wish_items/create$', views.create, name="create_wish"),
    url(r'^addwish/(?P<wish_id>[0-9]+)$', views.add_wish, name="add_wish"),
    url(r'^removewish/(?P<wish_id>[0-9]+)$', views.remove_wish, name="remove_wish"),
    url(r'^wish_items/(?P<wish_id>[0-9]+)$', views.show_wish, name="show_wish"),
    url(r'^delete/(?P<wish_id>[0-9]+)$', views.delete, name="delete")
]