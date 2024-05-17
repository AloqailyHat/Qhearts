from django.db import models
from django.utils import timezone

class RescueReport(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.URLField()
    situation = models.TextField()
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    animal_type = models.CharField(max_length=50)
    behavior = models.CharField(max_length=10, choices=[('friendly', 'Friendly'), ('aggressive', 'Aggressive')])
    keep_at_place = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    bring_to_shelter = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    adopt_after_treatment = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
