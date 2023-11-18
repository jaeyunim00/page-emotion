# sentiment_analysis/views.py

from django.shortcuts import render
from .utils import get_youtube_comments, analyze_sentiment

def index(request):
    return render(request, 'index.html')

def get_comments(request):
    if request.method == 'POST':
        video_url = request.POST.get('video_url')
        comments = get_youtube_comments(video_url)
        sentiment_result = analyze_sentiment(comments)
        print(sentiment_result)
        
        return render(request, 'comments.html', {'comments': comments, 'sentiment_result': sentiment_result})

    return render(request, 'index.html')
