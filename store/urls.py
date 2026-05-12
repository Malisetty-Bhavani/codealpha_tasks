from django.urls import path
from .views import *

urlpatterns = [

    path('', home),

    path('login/', login_view),

    path('signup/', signup_view),

    path('add-to-cart/<int:product_id>/',
         add_to_cart,
         name='add_to_cart'),

    path('cart/', cart_view),

    path('confirm-order/',
         confirm_order,
         name='confirm_order'),
]