# library_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from library import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'borrowers', views.BorrowerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('library.urls')),  # Tambahkan ini untuk mengarahkan ke aplikasi library
]
