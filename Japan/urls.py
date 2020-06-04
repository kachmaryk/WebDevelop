from django.urls import path
from .views import ContactListView, ContactDelete

urlpatterns = [
    path('', ContactListView.as_view(), name = "contact_list"),
    path('<str:id>/delete/', ContactDelete.as_view(), name = "contactDelete"),
]