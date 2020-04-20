from django.db import models
from django.db.models import Manager
from django.contrib.auth.models import User


class ModelBase(models.Model):
    """
    Model to save created at and updated at time and date
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class Article(ModelBase):
    """
    Model to save article added by django default user
    """
    POOR = 1
    AVERAGE = 2
    GOOD = 3
    VGOOD = 4
    EXCELLENT = 5
    RATING_CHOICES = (
        (POOR, "Poor"),
        (AVERAGE, "Average"),
        (GOOD, "Good"),
        (VGOOD, "Very Good"),
        (EXCELLENT, "Excellent")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    title = models.CharField(max_length=255)
    review = models.TextField()
    image_url = models.FileField(upload_to='uploaded_images/')
    imdb_rating =models.FloatField()

    objects = Manager()

    def __str__(self):
        return f"{self.title}"
