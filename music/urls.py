from django.urls import path
from .import views
app_name = 'music'
urlpatterns = [
    path("", views.index, name="index"),
    path(r'<album_id>/', views.detail, name='detail'),

]
