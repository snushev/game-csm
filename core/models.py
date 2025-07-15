from django.db import models

# Create your models here.

class NewPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
