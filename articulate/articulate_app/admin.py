from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect
from django.urls import path
from django.utils.safestring import mark_safe
from sentence_transformers import SentenceTransformer

from articulate_app.models import Article

admin.site.unregister([Group, User])
admin.site.site_header = "Articulate by apurvChaudhary"
admin.site.site_url = "/"

model = SentenceTransformer("all-mpnet-base-v2")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "type", "rating", "generate_embeddings_button"]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [path("generate_all_embeddings/", self.admin_site.admin_view(self.generate_all_embeddings))]
        return custom_urls + urls

    def generate_embeddings_button(self, obj=None):
        return mark_safe(
            '<a class="button" href="/admin/articulate_app/article/generate_all_embeddings/">Generate Embeddings</a>'
        )

    generate_embeddings_button.short_description = "Generate Embeddings"
    generate_embeddings_button.allow_tags = True

    def generate_all_embeddings(self, request):
        for article in Article.objects.all():
            article.embedding = model.encode(article.review).tolist()
            article.save()
        self.message_user(request, "Embeddings generated for all articles!")
        return redirect("/admin/articulate_app/article/")
