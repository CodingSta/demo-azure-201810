from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog.views import post_list, post_detail, post_new, post_edit, post_delete
from shop.views import item_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', post_list),
    path('blog/<int:pk>/', post_detail),
    path('blog/new/', post_new),
    path('blog/<int:pk>/edit/', post_edit),
    path('blog/<int:pk>/delete/', post_delete),
    path('shop/', item_list),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
