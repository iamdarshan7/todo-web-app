from django.urls import path
from tasks import views

urlpatterns =[
    path('', views.index, name='list'),
    path('update_task/<str:pk>',views.update_task, name="update_me"),
    path('delete_task/<str:pk>', views.delete_task, name='delete_me')
]