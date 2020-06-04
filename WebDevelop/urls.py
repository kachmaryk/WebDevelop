from django.contrib import admin
from django.urls import path, include
from Japan.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home_view'),
    path('winter/', winter_view, name='winter_view'),
    path('spring/', spring_view, name='spring_view'),
    path('summer/', summer_view, name='summer_view'),
    path('autumn/', autumn_view, name='autumn_view'),
    path('signIn/', signIn_view, name='signIn_view'),
    path('signUp/', signUp_view, name='signUp_view'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact_list/', include("Japan.urls"), name = "contact_list")
]
