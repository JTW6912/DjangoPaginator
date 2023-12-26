from django.urls import path,include
from . import views

urlpatterns = [
    path('list/',views.list),
    path('page/list/', views.page_list),
]