from django.db.models import ObjectDoesNotExist

from articulate_app.models import Article
from articulate_app.serializers import ArticleSerializer


def get_home_page():
    return ArticleSerializer(Article.objects.order_by("-created_at"), many=True).data


def get_movie_data(article_id):
    try:
        article_serializer = ArticleSerializer(Article.objects.get(id=article_id))
        return None, article_serializer.data
    except ObjectDoesNotExist:
        return f"No article found with this id : {article_id}", None


def get_related_articles(article_id: int, top_k: int = 5):
    """
    Return up to `top_k` semantically similar articles to the given article_id using MariaX similarity search.
    Falls back to recent articles when the source article has no embedding or when not enough neighbors exist.
    """
    try:
        src = Article.objects.get(id=article_id)
    except ObjectDoesNotExist:
        return []

    # If the source article has an embedding, use similarity search; otherwise fall back
    results = []
    if src.embedding:
        # Fetch top_k + 1 to account for the source article possibly appearing in results
        neighbors = (
            Article.objects.similarity_search(
                src.embedding, top_k=top_k + 1, metric="cosine", prefilter={"embedding__isnull": False}
            )
        )
        # Exclude the source article
        results = [a for a in neighbors if a.id != src.id][:top_k]

    # Fallback if no embedding or insufficient results
    if len(results) < top_k:
        needed = top_k - len(results)
        fallback_qs = Article.objects.exclude(id=src.id).order_by("-created_at")[:needed]
        # Avoid duplicates if some neighbors already included
        existing_ids = {a.id for a in results}
        results.extend([a for a in fallback_qs if a.id not in existing_ids])

    return ArticleSerializer(results, many=True).data


def get_high_to_low():
    return ArticleSerializer(Article.objects.order_by("-rating", "-created_at"), many=True).data


def get_low_to_high():
    return ArticleSerializer(Article.objects.order_by("rating", "-created_at"), many=True).data
