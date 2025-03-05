from django.shortcuts import render
from django.core.paginator import Paginator
import requests

# Create your views here.

def get_characters(request):
    api_url = "https://last-airbender-api.fly.dev/api/v1/characters"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        characters = response.json()
    else:
        characters = []

    paginator = Paginator(characters, 10)

    page = request.GET.get('page')
    characters = paginator.get_page(page)
    
    return render(request, "index.html", {"characters": characters})
