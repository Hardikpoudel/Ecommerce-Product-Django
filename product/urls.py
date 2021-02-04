

from django.urls import path
from product import views
from django.views.generic import TemplateView
from product.views import list, detail

urlpatterns = [
    path('', list.as_view(), name="list"),
    path('<pk>', detail.as_view(), name="detail")
]
