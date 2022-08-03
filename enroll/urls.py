from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all, name="addshow"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update"),
]
