from django.urls import path
from .views import landing_page, price_guide, pokemon_page, lorcana_page, wwe_page, my_collection, card_sniper

urlpatterns = [
    path('', landing_page, name='landing'),
    path('price-guide/', price_guide, name='price_guide'),
    path('pokemon/', pokemon_page, name='pokemon'),
    path('lorcana/', lorcana_page, name='lorcana'),
    path('wwe/', wwe_page, name='wwe'),
    path('my-collection/', my_collection, name='my_collection'),
    path('card-sniper/', card_sniper, name='card_sniper'),
]
