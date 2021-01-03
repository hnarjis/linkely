from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count
from links.models import Article


class Command(BaseCommand):
    help = "Deletes duplicated articles and saves the oldest one"

    def handle(self, *args, **options):
        duplicate_urls = (
            Article.objects.values("url")
            .annotate(url_counts=Count("url"))
            .filter(url_counts__gt=1)
            .values_list("url")
        )

        duplicate_url_count = duplicate_urls.count()

        total_deleted = 0
        for (duplicate_url,) in duplicate_urls:
            duplicate_articles = Article.objects.filter(url=duplicate_url).order_by(
                "id"
            )
            exclude_id = duplicate_articles.first().id
            articles_to_delete = duplicate_articles.exclude(id=exclude_id)
            delete_count, _ = articles_to_delete.delete()
            total_deleted += delete_count

        self.stdout.write(
            self.style.SUCCESS(
                f"Deleted {total_deleted} duplicate articles leaving {duplicate_url_count} unique ones."
            )
        )
