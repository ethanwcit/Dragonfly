from django.urls import path
from.import views
app_name = "task"
urlpatterns = [
    path('',views.task_list, name="list"),
    path("create/", views.task_create, name="create"),
    path('<slug:slug>/', views.task_detail, name="detail"),
    path('markasdone/<slug:slug>/', views.markasdone, name="markasdone"),
]
