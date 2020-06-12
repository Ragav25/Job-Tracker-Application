from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    company = models.TextField()
    role = models.TextField()
    date_applied = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company
