from django.shortcuts import render
from datetime import date
from .models import Code, Tag
from django.db.models import F
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(['GET'])
def inicio(request):
    tags = Tag.objects.all()
    languages = Code.LANGUAGE_CHOICES
    return render(request, 'inicio.html', {'max_to_date': date.today().__str__(), 'tags': tags, 'languages': languages})