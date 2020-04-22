from django.db import models
from django.db.models import Manager
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    kb_limit = 80
    if filesize > kb_limit*1024:
        raise ValidationError(f"Max file size is {kb_limit}kb")


def validate_rating(num):
    limit = 5
    if num <= 0 or num > limit:
        raise ValidationError(f"Rating can vary in 0.1 to {limit}")
    elif len(tuple(str(num))) > 3:
        raise ValidationError("Upto one decimal eg. 1.1(correct) 1.11(wrong)")


def validate_imdb_rating(num):
    limit = 10
    if num <= 0 or num > limit:
        raise ValidationError(f"Rating can vary in 0.1 to {limit}")
    elif len(tuple(str(num))) > 3:
        raise ValidationError("Upto one decimal eg. 1.1(correct) 1.11(wrong)")


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
    TYPE_CHOICE = {
        ("Series", "SERIES"),
        ("Documentary", "DOCUMENTARY"),
        ("Short Film", "SHORT FILM"),
        ("Youtube", "YOUTUBE"),
        ("Movie", "MOVIE"),
        ("Album", "ALBUM"),
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(verbose_name="My Rating", validators=[validate_rating])
    title = models.CharField(verbose_name="Title", max_length=255)
    type = models.CharField(verbose_name="Type", max_length=50, choices=TYPE_CHOICE, default=0)
    creatives = models.CharField(verbose_name="Director/Creation/Youtuber", max_length=100, default="Not Mentioned")
    review = models.TextField(verbose_name="Review Text")
    embed_link = models.URLField(verbose_name="Trailer Embed Link", blank=True, null=True)
    image_url = models.FileField(verbose_name="Movie Poster", upload_to='uploaded_images/', validators=[validate_image],
                                 help_text='Maximum file size allowed is 80kb', unique=True)
    imdb_rating =models.FloatField(verbose_name="IMDB Rating", validators=[validate_imdb_rating])

    objects = Manager()

    def save(self, *args, **kwargs):
        if self.embed_link:
            youtube_normal_link = self.embed_link.split("&")[0]
            hash = youtube_normal_link.split("=")[1]
            youtube_embed_url = "https://www.youtube.com/embed/" + hash
            self.embed_link = youtube_embed_url
            super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
