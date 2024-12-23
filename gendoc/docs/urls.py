from django.urls import path
from .views import database_docs

urlpatterns = [
    path('database/', database_docs, name='database_docs'),
]