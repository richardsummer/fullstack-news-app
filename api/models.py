from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=60)
    body = models.CharField(max_length=60)

    def __str__(self):
        return self.title
        return self.body
