from django.urls import path
from . import views
urlpatterns = [
    path('', views.contactlist, name='contactlist'),
    path('<int:contact_id>/', views.contactdetail, name='contactdetail'),
]
