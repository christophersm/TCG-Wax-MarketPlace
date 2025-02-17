from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, "landing.html")

def price_guide(request):
    return render(request, "price_guide.html")

def pokemon_page(request):
    return render(request, "pokemon.html")

def lorcana_page(request):
    return render(request, "lorcana.html")

def wwe_page(request):
    return render(request, "wwe.html")

def my_collection(request):
    return render(request, "my_collection.html")

def card_sniper(request):
    return render(request, "card_sniper.html")

