from django.db import models
from django.template.defaultfilters import slugify


class Job(models.Model):
    title = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    description = models.CharField(max_length=256, unique=False)
    company_name = models.CharField(max_length=128, default='')
    contact_email = models.EmailField(default='')
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title