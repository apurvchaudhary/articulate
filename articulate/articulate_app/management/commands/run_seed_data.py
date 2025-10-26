import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from articulate_app.models import Article


class Command(BaseCommand):
    help = "Seed 6 Article objects with simple titles/reviews. Idempotent: skips existing (same user+title)."

    def handle(self, *args, **options):
        _user = get_user_model()
        username, email, password = "admin", "admin@example.com", "admin1234"
        user, created = _user.objects.get_or_create(
            username=username,
            defaults={"email": email}
        )
        if created:
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Superuser Created: {username}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' already exists."))

        if user is None:
            raise CommandError("No users found. Please create a user before running this command.")

        pairs = [
            ("Happy family", "this is good movie"),
            ("Happy Ending", "It is a good one"),
            ("Happy Birthday", "Good one to watch"),
            ("Sad family", "very bad"),
            ("Sad Ending", "worst and bad"),
            ("Sad Birthday", "very sad"),
        ]

        created = 0
        skipped = 0
        for title, review in pairs:
            obj, was_created = Article.objects.get_or_create(
                user=user,
                title=title,
                defaults={
                    "review": review,
                    "rating": round(random.uniform(0.1, 5.0), 1),
                    "imdb_rating": round(random.uniform(0.1, 10.0), 1),
                    "image": None,
                },
            )
            if was_created:
                created += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {title}"))
            else:
                skipped += 1
                self.stdout.write(self.style.WARNING(f"Skipped (already exists): {title}"))

        self.stdout.write(self.style.SUCCESS(f"Done. Created: {created}, Skipped: {skipped}. Total intended: {len(pairs)}"))
