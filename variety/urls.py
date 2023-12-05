from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('signup', views.signup, name="signup"),
    path('register', views.register, name="register"),
    path('place',views.place,name="place"),
    path('cart', views.cart, name="cart"),
    path('store', views.store, name="store"),
    path('product',views.product,name="product"),
    path('product-detail', views.productdet, name="productdet"),
    path('search', views.search, name="search"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('order-complete',views.order_complete,name="order_compleate"),
]
