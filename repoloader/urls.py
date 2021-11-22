"""
repoloader URL Configuration

"""
from django.contrib import admin
from django.urls import path
from repoloader import views

# for heruko
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("get_repo", views.get_repo, name="get_repo"),
    path("downloaded_to_csv", views.downloaded_to_csv, name="downloaded_to_csv"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
