from apps import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('home/', views.home, name="home"),
    path('home/contact', views.contact, name="contact"),
    path('home/register', views.register_request, name="register"),
    path('home/login', views.login_request,name="login"),
    path('home/product', views.shopnow,name="product"),
    path('home/cart', views.add_to_cart,name="cart"),
    path('delete/<int:id>', views.delete,name="delete"),
    path("home/logout", views.logout_request, name="logout"),
    path("get_cart_data",views.get_cart_data,name="get_cart_data"),
    path("change_quan",views.change_quan,name="change_quan"),
]
