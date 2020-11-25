from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # return the title as string by using magic method
    def __str__(self) -> str:
        return self.title

    # return to the post detail after creating new post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
