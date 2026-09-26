from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    status = models.CharField(max_length=60, blank=True,
        help_text='e.g. "Full-Stack Project"')
    description = models.TextField()
    meta_description = models.CharField(max_length=160, blank=True,
        help_text="SEO description (max 160 chars). Blank = auto from description.")
    tech_stack = models.CharField(max_length=250,
        help_text="Comma separated, e.g. HTML, CSS, Django")
    image = models.ImageField(upload_to="projects/%Y/%m/", blank=True)
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:220]
            slug, i = base, 1
            while Project.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]

    def get_absolute_url(self):
        return reverse("projects:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title