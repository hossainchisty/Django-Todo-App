from django.urls import  path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('update_task/<str:pk>', views.update_tasks, name="update"),
    path('delete_task/<str:pk>/', views.delete_tasks, name="delete_task")
]