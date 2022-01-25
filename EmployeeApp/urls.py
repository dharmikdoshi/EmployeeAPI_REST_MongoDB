from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^employee$', views.employeeApi),
    url(r'^employee/([0-9]+)$',views.employeeApi)          
]


