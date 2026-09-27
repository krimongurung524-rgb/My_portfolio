from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from projects.models import Project


class ProjectSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Project.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0

    def items(self):
        return ["home"]

    def location(self, item):
        return reverse(item)