from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def about(request):
    return HttpResponse("This is the about page.")  


# parametoers in URL 
def search(request, keyword, page):
    return HttpResponse(f"Search results for '{keyword}' on page {page}.")  

def date(request, year, month, day):
    return HttpResponse(f"Date: {year}-{month:02d}-{day:02d}")

# Regex paths
def year_archive(request, year):
    return HttpResponse(f"Articles from the year {year}.")  

def month_archive(request, year, month):
    return HttpResponse(f"Articles from {year}-{int(month):02d}.")