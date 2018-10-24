from django.contrib import admin
from django.urls import path

from blog.views import post_list
from shop.views import item_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', post_list),
    path('shop/', item_list),
]
