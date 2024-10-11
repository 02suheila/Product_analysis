from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
 
    path('details/<str:platform>/', views.details, name='details'),
    path('all_details/' ,views.all_details, name = 'all_details'),

]