from django.urls import path, include
from . import views


urlpatterns =[
    path('produntion/api-produntion', include('rest_framework.urls')),
    path('province', views.ProvinceView.as_view()),
    path('producer',views.ProducerView.as_view()),
    path('producer/<province_code>',views.ProducerListView.as_view())
 ]