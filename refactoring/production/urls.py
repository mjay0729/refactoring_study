from django.urls import path, include
from . import views


urlpatterns =[
    path('production/api-produntion', include('rest_framework.urls')),
    path('province', views.ProvinceView.as_view()),
    path('province/demand/<province_code>', views.ProvinceDemandView.as_view()),
    path('province/shortfall/<province_code>', views.ProvinceShortfallView.as_view()),
    path('province/profit/<province_code>', views.ProvinceProfitView.as_view()),
    path('province/profit/<province_code>', views.ProvinceProfitView.as_view()),
    path('producer',views.ProducerView.as_view()),
    path('producer/<province_code>',views.ProducerListView.as_view()),
    path('producer/production/<producer_name>',views.ProducerProductionView.as_view())
 ]