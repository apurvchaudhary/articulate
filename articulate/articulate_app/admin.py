from django.contrib import admin
from django.contrib.auth.models import Group, User
from articulate_app.models import Article
from django.urls import path
from django.shortcuts import redirect

# Register your models here.
admin.site.register([Article])
admin.site.unregister([Group, User])
admin.site.site_header = "Admin by Apurv"
admin.site.site_url = ""

from django.contrib import admin
from articulate_app.models import Article
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "type", "rating"]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('generate_all_embeddings/', self.admin_site.admin_view(self.generate_all_embeddings))
        ]
        return custom_urls + urls

    def generate_all_embeddings(self, request):
        for article in Article.objects.all():
            article.embedding = model.encode(article.review).tolist()
            article.save()
        self.message_user(request, "Embeddings generated for all articles!")
        return redirect("/admin/articulate_app/article/")