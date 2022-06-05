from django.db import models
from config.settings import SITE_URL


class Link(models.Model):
    base_url = models.URLField()
    code = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    usage_count = models.PositiveIntegerField(default=0)

    @property
    def short_url(self):
        return SITE_URL + self.code
