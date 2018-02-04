from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('opt-in/', include('optin.urls')),
    path('opt-out/', include('optout.urls')),
]
