from django.db import models
from django.db.models import Manager
from django.core.cache import cache
from django.contrib.auth.models import User

from articulate_app.validators import validate_image, validate_rating, validate_imdb_rating
from articulate_app.service import create_embed_link


class Article(models.Model):
    """
    Model to save article added by django default user
    """
    TYPE_CHOICE = [
        ("Series", "series"),
        ("Documentary", "documentary"),
        ("Short Film", "short Film"),
        ("Youtube", "youtube"),
        ("Movie", "movie"),
        ("Album", "album"),
    ]
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Select yourself from dropdown')
    rating = models.FloatField(verbose_name="Your Rating", validators=[validate_rating], help_text='Decimal 0.1 to 5.0')
    title = models.CharField(verbose_name="Title", max_length=255, help_text='Keep 1st letter Capital')
    type = models.CharField(verbose_name="Type", max_length=50, choices=TYPE_CHOICE, default=TYPE_CHOICE[4][0],
                            help_text='default is Movie')
    creatives = models.CharField(verbose_name="Director/Creation/Youtuber", max_length=100, default="Not Mentioned")
    review = models.TextField(verbose_name="Review Text")
    embed_link = models.URLField(verbose_name="Trailer Youtube Link", blank=True, null=True, help_text='Paste only youtube urls')
    image_url = models.FileField(verbose_name="Movie Poster", upload_to='uploaded_images/', validators=[validate_image],
                                 help_text='Maximum file size allowed is 80kb', unique=True)
    imdb_rating = models.FloatField(verbose_name="IMDB Rating", validators=[validate_imdb_rating],
                                    help_text='Decimal 0.1 to 10.0')

    objects = Manager()

    def save(self, *args, **kwargs):
        if self.embed_link:
            self.embed_link = create_embed_link(link=self.embed_link)
        cache.clear()
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
