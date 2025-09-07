from django.db import models

# Create your models here.

python

from django.db import models

class SearchResult(models.Model):
    # The user's query that triggered this search result.
    query = models.CharField(max_length=255)
    # The title of the search result.
    title = models.CharField(max_length=255)
    # The URL of the search result.
    link = models.URLField()
    # A short description or snippet.
    snippet = models.TextField()
    # The source search engine (e.g., 'Google', 'Bing').
    source = models.CharField(max_length=50)
    # A custom score to rank the results.
    relevance_score = models.FloatField(default=0.0)
    # The timestamp of when the result was created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.source})"
