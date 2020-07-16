from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('success', 'Success'),
    ('not-selected', 'Not-Selected'),
    ('interviewing', 'Interviewing'),
]

class Post(models.Model):
    company = models.TextField()
    role = models.TextField()
    date_applied = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='', verbose_name="status", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company

    # def get_absolute_url(self):
    #     return reverse('jobTrack-home')
