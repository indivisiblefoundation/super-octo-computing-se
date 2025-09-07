from django.shortcuts import render

def index(request):
    return render(request, 'search/index.html')

# Create your views here.

python

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import SearchResult
from .tasks import run_spider_task  # Assumes you are using Celery or a similar task queue

# A dictionary mapping query terms to a source engine.
# In a real app, this would be determined by user input or more complex logic.
SOURCE_ENGINES = {
    'google': 'GoogleSpider',
    'bing': 'BingSpider',
}

def index(request):
    """
    Renders the search form page.
    """
    return render(request, 'search/index.html')


def search_results(request):
    """
    Handles the search query, triggers scraping, and displays results.
    """
    query = request.GET.get('q', '').strip()
    source = request.GET.get('source', '')
    results = []

    if query:
        # **Step 1: Execute scraping in a background task (recommended)**
        # This prevents the web page from waiting for the scraper to finish.
        # It's especially crucial for a meta-spider, which needs to contact external sites.
        if source:
            # You can trigger a specific spider based on user input.
            run_spider_task.delay(query, source)
        else:
            # Or run all spiders and combine results later.
            for engine in SOURCE_ENGINES.values():
                run_spider_task.delay(query, engine)

        # **Step 2: Fetch and display results (This example is simplified)**
        # In a more advanced setup, you would check task status
        # and display "loading" messages or use a real-time framework.
        # For now, we'll assume the results are ready to be queried from the database.
        
        # A meta-spider aggregates results from different sources.
        # You would typically have a model that stores results from each engine.
        # We'll use a simplified model 'SearchResult' for this example.
        results_queryset = SearchResult.objects.filter(query__icontains=query).order_by('-relevance_score')

        # **Step 3: Implement pagination**
        paginator = Paginator(results_queryset, 10)  # Show 10 results per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'query': query,
            'page_obj': page_obj,
        }
        return render(request, 'search/results.html', context)
    
    # Render the initial search page if no query was provided
    return render(request, 'search/index.html')


