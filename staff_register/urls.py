from django.urls import path, include
from . import views 

urlpatterns = [
    path('',views.staff_form),
    path('list/',views.staff_list),
]
