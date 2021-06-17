from pathlib import Path
from django.http import HttpResponse
from django.views.generic import TemplateView


def helloworldfunction(request):
    return HttpResponse("<h1> Hello WOrld </h1>")


class helloworldclass(TemplateView):
    template_name = 'hello.html'
