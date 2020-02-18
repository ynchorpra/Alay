
from django.urls import path
from . import views

app_name = 'mymodule' # So we can use it like: {% url 'mymodule:user_register' %} on our template.
urlpatterns = [
    path("", views.user_register, name="user_register"),

]