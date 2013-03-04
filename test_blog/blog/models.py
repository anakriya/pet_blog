from django.db import models

# Create your models here.
class Article(models.Model):
    pub_date = models.DateTimeField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)

    def __unicode__(self):
        return self.headline