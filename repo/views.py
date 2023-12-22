from django.shortcuts import render, redirect
from datetime import date
from .models import Code, Tag
from django.db.models import F
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
import os
from django.contrib.sessions.models import Session
# Create your views here.

@require_http_methods(['GET'])
def inicio(request):
    tags = Tag.objects.all()
    languages = Code.LANGUAGE_CHOICES
    return render(request, 'inicio.html', {'max_to_date': date.today().__str__(), 'tags': tags, 'languages': languages})

@require_http_methods(['GET'])
def page_not_found(request, exception):
    return render(request, '404.html', {'exception': exception})

@require_http_methods(['GET', 'POST'])
def preferences(request):
    if request.method == 'GET':
        themes = os.listdir(os.path.join('templates', 'static', 'js', 'codemirror', 'theme'))
        themes = list(map(lambda x: x.split('/')[-1].split('.')[0], themes))
        return render(request, 'preferences.html', {'themes': themes})
    else:
        codeTheme = request.POST.get('codeTheme')
        backgroundTheme = request.POST.get('backgroundTheme', 'off')
        request.session['codeTheme'] = codeTheme
        request.session['backgroundTheme'] = backgroundTheme
        return redirect('repo_preferences')
