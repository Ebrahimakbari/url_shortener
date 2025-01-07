from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from .models import UrlShortener
from .forms import UrlShortenerForm



class UrlShortenerView(View):
    form_class = UrlShortenerForm
    template = 'urlshortener/url_shortener_view.html'
    model_class = UrlShortener
    
    def get(self, request:HttpRequest):
        context = {
            'form':self.form_class()
        }
        return render(request, self.template, context)
    
    def post(self, request:HttpRequest):
        url_data = self.form_class(request.POST)
        if url_data.is_valid:
            url_obj = url_data.save()
            shortened_url = request.build_absolute_uri('/') + url_obj.short_url
            
            context = {
                'original_url':url_obj.original_url,
                'short_url':shortened_url
            }
            return render(request, self.template, context)
        
        context = {
            'errors':url_data.errors
        }
        return render(request, self.template, context)

