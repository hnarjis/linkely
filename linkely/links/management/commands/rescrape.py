from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count
from links.models import Article
from links.scraper import ScraperError
from links.wiring import es_client, TransportError


class Command(BaseCommand):
    help = "Scrape all articles that haven't been indexed."

    def handle(self, *args, **options):
        # candidates = Article.objects.filter(title="")
        candidates = Article.objects.all()
        success = 0
        fail = 0

        es = es_client()

        for article in candidates:
            try:
                found = es.get(
                    index="articles",
                    id=article.id,
                    doc_type="article",
                    _source=False,
                )["found"]
                if found:
                    self.stdout.write(f"Skipping existing article {article.url}")
                    continue
            except TransportError:
                pass

            self.stdout.write(f"Rescraping {article.url}")

            try:
                article.scrape()
                success += 1
            except ScraperError as ex:
                fail += 1
                self.stdout.write(
                    self.style.NOTICE(f"Could not scrape {article.url}: {ex}")
                )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully scraped {success} articles and failed to scrape {fail}."
            )
        )
