from django.conf import settings
from random import choice
from string import ascii_letters, digits

url_shortener_size = getattr(settings, 'MAX_URL_SHORTENER_SIZE', 5)
chars = ascii_letters + digits



def create_random_str(chars):
    return ''.join(choice(chars) for _ in range(url_shortener_size))


# checking for duplicate possibility of short urls
def shortener_url_generator(model_instance):
    random_str = create_random_str(chars)
    
    model = model_instance.__class__
    if model.objects.filter(short_url=random_str).exists():
        shortener_url_generator(model_instance)
    return random_str