from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main),
    path('about/', views.about),
    path('promotion/', views.promotion),
    path('store/', views.store),
    path('mitr/', views.mitr),
    path('hanuman/', views.hanuman),
    path('kraithong/', views.kraithong),
    path('nagas/', views.nagas),
    path('erawan/', views.erawan),
    path('tossakan/', views.tossakan),
    path('cart/', views.cart),
    path('checkout/', views.checkout)
]
