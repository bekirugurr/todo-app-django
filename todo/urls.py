from django.urls import path
from .views import home, update, change_is_done, delete

urlpatterns = [
    path('', home, name="home"),
    path('update/<int:id>', update, name="update"),
    path('change_is_done/<int:id>', change_is_done, name="change_is_done"),
    path('delete/<int:id>', delete, name="delete"),
]