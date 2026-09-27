from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=150)
    icon_class = models.CharField(max_length=60,
        help_text='Devicon class, e.g. "devicon-html5-plain"')
    color_class = models.CharField(max_length=60,
        help_text='Your CSS class, e.g. "html-icon"')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class Education(models.Model):
    period = models.CharField(max_length=50)
    degree = models.CharField(max_length=120)
    institution = models.CharField(max_length=150)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.degree


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} — {self.created_at:%Y-%m-%d}"
