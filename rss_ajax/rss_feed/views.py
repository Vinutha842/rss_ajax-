import feedparser
from django.http import JsonResponse
from django.shortcuts import render

def fetch_rss(request):
    url = 'http://feeds.bbci.co.uk/news/rss.xml'  
    # Replace with your RSS feed URL
    feed = feedparser.parse(url)
    print("Feed Status:", feed.status)
    print("Feed Entries:", len(feed.entries))
    
    entries = [{
        'title': entry.title,
        'link': entry.link,
        'summary': entry.summary
    } for entry in feed.entries]
    
    print("Parsed Entries:", entries)
    
    return JsonResponse(entries, safe=False)

def index(request):
    return render(request, 'index.html')
