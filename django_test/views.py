from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    vars = {
    "title": "Welcome to My Django Site",
    "content": "This is the home page of my awesome Django test project. Explore the different URL patterns and see how Django routing works!",
}
    return render(request, "test.html", vars)

def index(request):
    context = {
        "title": "Welcome to My Django Site",
        "content": "This is the home page of my awesome Django test project. Explore the different URL patterns and see how Django routing works!",
    }
    return render(request, "index.html", context)

def about(request):
    # return HttpResponse("This is the about page.")  
    return render(request, "about.html")


# Parameters in URL 
def search(request, keyword, page):
    return HttpResponse(f"Search results for '{keyword}' on page {page}.")  

def date(request, year, month, day):
    return HttpResponse(f"Date: {year}-{month:02d}-{day:02d}")

# Regex paths
def year_archive(request, year):
    return HttpResponse(f"Articles from the year {year}.")  

def month_archive(request, year, month):
    return HttpResponse(f"Articles from {year}-{int(month):02d}.")

def maps(request):
    type = request.GET.get("type", "roadmap")
    lat = request.GET.get("lat", "13.7245")
    lon = request.GET.get("lon", "100.49.30")   
    zoom = request.GET.get("zoom", "11") 
    query = request.GET.get("q", "")
    return HttpResponse(f"Map type: {type}, Latitude: {lat}, Longitude: {lon}, Zoom: {zoom}, Query: {query}")

