from django.db import models

# Create your models here.
class Snippet(models.Model):
    slug = models.CharField(max_length=200)
    html = models.TextField()
    
    def __unicode__(self):
        return self.slug
