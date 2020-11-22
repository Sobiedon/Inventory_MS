from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),

    re_path('index', views.index, name='index'),
    path('inventory/', views.inventory, name='inventory'),
    path('checkout/', views.checkout, name='checkout'),
    path('transaction/', views.transaction, name='transaction'),
    path('report/', views.report, name='report'),
    path('chart/', views.chart, name='chart'),
    path('admin/', admin.site.urls),
]
