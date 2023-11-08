from django.shortcuts import render, redirect
from .models import Tag
from urllib.parse import urlencode
from django.urls import reverse
from unidecode import unidecode
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(['POST'])
def delete(request, pk):
    Tag.objects.filter(pk = pk).delete()
    return redirect(reverse('repo_inicio'))

@require_http_methods(['GET', 'POST'])
def upd(request, pk):
    if request.method == 'GET':
        try:
            tag = Tag.objects.get(pk = pk)
            return render(request, 'tag/upd.html', {'tag': tag})
        except ObjectDoesNotExist as ex:
            return render(request, '404.html', {'message': ex})
    else:
        human_name = request.POST.get('name')
        name = unidecode(human_name).lower()
        description = request.POST.get('description')
        tag = Tag.objects.filter(pk = pk).update(human_name = human_name, name = name, description = description)
        return redirect(reverse('repo_tag_upd', args = [pk]))

@require_http_methods(['GET', 'POST'])
def add(request):
    if request.method == 'GET':
        return render(request, 'tag/add.html')
    else:
        human_name = request.POST.get('name')
        name = unidecode(human_name).lower()
        description = request.POST.get('description')
        tag = Tag(name = name, human_name = human_name, description = description)
        tag.save()
        return redirect(reverse('repo_tag_add'))

@require_http_methods(['GET'])
def tag_results(request, key):
    MAX_ITEMS_PER_PAGE = 8

    page = int(request.GET.get('page', 1))
    asc = int(request.GET.get('asc', 1))

    low = (page - 1) * MAX_ITEMS_PER_PAGE
    high = page * MAX_ITEMS_PER_PAGE

    try:
        tag = Tag.objects.get(pk = key)
    except ObjectDoesNotExist as ex:
        return render(request, '404.html', {'message': ex})

    total_results = tag.code_set.count()

    sources = tag.code_set.order_by(['-', ''][asc] + 'createdAt')[low : high]

    URL_FLIP_CREATEDAT_PARAMS = {'page': page, 'asc': asc ^ 1}
    URL_FLIP_CREATEDAT = f"{reverse('repo_tag_view', args = [key])}?{urlencode(URL_FLIP_CREATEDAT_PARAMS)}"

    URL_PREVIOUS_PARAMS = {
        'page': page - 1,
        'asc': asc
    }

    URL_PREVIOUS = f"{reverse('repo_tag_view', args = [key])}?{urlencode(URL_PREVIOUS_PARAMS)}"

    URL_NEXT_PARAMS = {
        'page': page + 1,
        'asc': asc
    }

    URL_FIRST_PARAMS = {'page': 1, 'asc': asc ^ 1}
    URL_FIRST = f"{reverse('repo_tag_view', args = [key])}?{urlencode(URL_FIRST_PARAMS)}"

    URL_NEXT = f"{reverse('repo_tag_view', args = [key])}?{urlencode(URL_NEXT_PARAMS)}"

    URL_PAGES = []

    start_delta = max(1, page - 2) - page

    for delta in range(start_delta, start_delta + 5):
        p = page + delta
        if p > 0 and (p - 1) * MAX_ITEMS_PER_PAGE < total_results:
            URL_PARAMS = {'page': p, 'asc': asc}
            URL = f"{reverse('repo_tag_view', args = [key])}?{urlencode(URL_PARAMS)}"
            URL_PAGES.append((p, p == page , URL))

    return render(request, 'tag/tag.html', {'tag' : tag,
    'sources' : sources,
    'URL_FLIP_CREATEDAT': URL_FLIP_CREATEDAT,
    'asc' : asc,
    'URL_PAGES': URL_PAGES,
    'total_results': total_results,
    'URL_PREVIOUS': URL_PREVIOUS if page > 1 else None,
    'URL_NEXT': URL_NEXT if page * MAX_ITEMS_PER_PAGE < total_results else None,
    'URL_FIRST': URL_FIRST if len(URL_PAGES) and URL_PAGES[0][0] > 1 else None
    })

@require_http_methods(['GET'])
def all_tags(request):
    tags = Tag.objects.order_by('name')
    rows = [[tags[k + i] for i in range(4) if k + i < len(tags)] for k in range(0, len(tags), 4)]
    return render(request, 'tag/all.html', {'tags' : rows})
