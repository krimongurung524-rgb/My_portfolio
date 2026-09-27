from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from core import views as core_views
from .sitemaps import ProjectSitemap, StaticViewSitemap

sitemaps = {"projects": ProjectSitemap, "static": StaticViewSitemap}

urlpatterns = [
    path("", core_views.home, name="home"),
    path("contact/", core_views.contact, name="contact"),
    path("projects/", include("projects.urls")),
    path("admin/", admin.site.urls),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path("robots.txt", TemplateView.as_view(
        template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
