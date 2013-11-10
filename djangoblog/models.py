from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    likes = models.IntegerField()
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title