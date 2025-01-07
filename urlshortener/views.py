from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import UrlShortener
from .forms import UrlShortenerForm
from django.db.models import F


class UrlShortenerView(View):
    form_class = UrlShortenerForm
    template = "urlshortener/url_shortener_view.html"

    def get(self, request: HttpRequest):
        context = {"form": self.form_class()}
        return render(request, self.template, context)

    def post(self, request: HttpRequest):
        url_data = self.form_class(request.POST)
        if url_data.is_valid:
            url_obj = url_data.save()
            shortened_url = request.build_absolute_uri("/") + url_obj.short_url

            context = {
                "form": self.form_class(),
                "original_url": url_obj.original_url,
                "short_url": shortened_url,
            }
            return render(request, self.template, context)

        context = {"errors": url_data.errors}
        return render(request, self.template, context)


class RedirectShortUrlView(View):
    def get(self, request, short_url):
        url_qs = UrlShortener.objects.filter(short_url=short_url)
        if url_qs.exists():
            url_obj = url_qs.first()
            url_obj.times_used = F('times_used') + 1
            url_obj.save()
            return redirect(url_obj.original_url)
        return HttpResponse("link is broken!!")
