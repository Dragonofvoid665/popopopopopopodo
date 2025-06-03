# users/admin.py
from django.contrib import admin
from shop.models import Product, Cart, CartItem
from users.models import User
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)