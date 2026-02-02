from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:contact_id>/', views.contact, name='contact'),
    path('<int:contact_id>/update/', views.update, name='update'),
]
