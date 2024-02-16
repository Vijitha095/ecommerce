"""
URL configuration for Ecommproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecommapp import views
# from django.conf import settings
# from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg',views.SignUpView.as_view(),name="reg"),
    path('log',views.SignInView.as_view(),name="login"),
    path('signout',views.SignOutView.as_view(),name="signout"),
    path('',views.HomeView.as_view(),name="home"),
    path('product_detail/<int:id>',views.ProductDetailView.as_view(),name="product_detail"),
    path('cart/<int:id>',views.AddToCartView.as_view(),name="add_cart"),
    path('cartlist',views.CartView.as_view(),name="cart_view"),
    path('placeorder/<int:cid>/<int:pid>',views.PlaceOrderView.as_view(),name="placeorder"),
    path('cart/delete/<int:id>',views.CartDeleteView.as_view(),name='cart_delete')
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

