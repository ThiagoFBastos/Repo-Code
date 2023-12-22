from django.shortcuts import render, redirect
from .models import Code, Tag
from django.db.models import Q, Exists, OuterRef, Count, Subquery, Value
from urllib.parse import urlencode
from django.urls import reverse
from unidecode import unidecode
from django.utils import timezone
import os
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist

# Create your views here

@require_http_methods(['GET'])
def source(request, key):
    try:
        code = Code.objects.get(pk = key)
        partial_tags = code.tags.all()[:3]
        languages = sorted(Code.LANGUAGE_CHOICES, key = lambda x: x[1])
        themes = os.listdir(os.path.join('templates', 'static', 'js', 'codemirror', 'theme'))
        css_files = list(map(lambda f: os.path.join('js', 'codemirror', 'theme', f), themes))
        themes = list(map(lambda t: t.split('.')[0], themes))
        print(request.session.get('codeTheme'))
        return render(request, 'code/code.html', {
            'source' : code, 
            'partial_tags': partial_tags, 
            'themes': themes, 
            'css_files': css_files, 
            'languages': languages
        })
    except ObjectDoesNotExist as ex:
        return render(request, '404.html', {'message': ex})

@require_http_methods(['GET', 'POST'])
def add(request):
    if request.method == 'GET':
        languages = sorted(Code.LANGUAGE_CHOICES, key = lambda x: x[1])
        tags = Tag.objects.values('id', 'human_name')
        themes = os.listdir(os.path.join('templates', 'static', 'js', 'codemirror', 'theme'))
        css_files = list(map(lambda f: os.path.join('js', 'codemirror', 'theme', f), themes))
        themes = list(map(lambda t: t.split('.')[0], themes))
        return render(request, 'code/add.html', {'languages': languages, 'tags': tags, 'themes': themes, 'css_files': css_files})

    else:
        title = request.POST.get('title')
        now = timezone.now()
        description = request.POST.get('description')
        source = request.POST.get('source')
        original = request.POST.get('original')
        language = request.POST.get('language')
        tags = list(map(int, request.POST.getlist('tags')))
        code = Code(description = description, title = title, createdAt = now, updatedAt = now, source = source, original = original, language = language)
        code.save()
        code.tags.set(tags)
        return redirect(reverse('repo_code_add'))

@require_http_methods(['GET'])
def search_by_keywords(request):
    title = request.GET.get('title', '')
    tags = list(map(int, request.GET.getlist('tags')))
    page = int(request.GET.get('page', 1))
    asc = int(request.GET.get('asc', 1)) 
    language = request.GET.get('language', '-1')
    fromDate = request.GET.get('fromDate', '0001-01-01')
    toDate = request.GET.get('toDate', timezone.now().date().__str__())
    textKeywords = request.GET.get('filterText', '').split()

    logicTag = request.GET.get('logicTag', 'AND')

    MAX_ITEMS_PER_PAGE = 8

    low = (page - 1) * MAX_ITEMS_PER_PAGE
    high = page * MAX_ITEMS_PER_PAGE

    condition = Q(title__contains = title) & Q(createdAt__date__range = (fromDate, toDate))

    sources = Code.objects.all()

    if len(tags):
        if logicTag == 'AND':
            print(sources)
            subquery = Tag.objects.filter(Q(id__in = tags) & Q(code__id = OuterRef("pk"))) \
            .annotate(placeholder = Value(1)) \
            .values('placeholder') \
            .annotate(sub_cnt = Count('id')) \
            .values('sub_cnt')
            sources = sources.annotate(sub_cnt = Subquery(subquery))
            sources = sources.filter(sub_cnt = len(tags))
        else:
            condition = condition & Q(tags__id__in = tags)

    if len(textKeywords):
        OR = Q(description__contains = textKeywords[0])
        for i in range(1, len(textKeywords)):
            OR = OR | Q(description__contains = textKeywords[i])
        condition = condition & OR

    if language != '-1': condition = condition & Q(language = language)

    sources = sources.filter(condition).distinct()

    sources = sources.order_by('createdAt') if asc == 1 else sources.order_by('-createdAt')

    total_results = sources.count()

    sources = sources[low : high]

    URL_FLIP_CREATEDAT_PARAMS = {'page': page,
                                 'asc': asc ^ 1,
                                 'title': title,
                                 'language': language,
                                 'fromDate': fromDate,
                                 'toDate': toDate,
                                 'tags': tags,
                                 'logicTag': logicTag
                                }

    URL_FLIP_CREATEDAT = f"{reverse('repo_search_by_keys')}?{urlencode(URL_FLIP_CREATEDAT_PARAMS, True)}"

    URL_PREVIOUS_PARAMS = {
        'title': title,
        'asc': asc,
        'page': page - 1,
        'language': language,
        'fromDate': fromDate,
        'toDate': toDate,
        'tags': tags,
        'logicTag': logicTag
    }

    URL_PREVIOUS = f"{reverse('repo_search_by_keys')}?{urlencode(URL_PREVIOUS_PARAMS, True)}"

    URL_NEXT_PARAMS = {
        'title': title,
        'asc': asc,
        'page': page + 1,
        'language': language,
        'fromDate': fromDate,
        'toDate': toDate,
        'tags': tags,
        'logicTag': logicTag
    }

    URL_NEXT = f"{reverse('repo_search_by_keys')}?{urlencode(URL_NEXT_PARAMS, True)}"

    URL_PAGES = []

    URL_FIRST_PARAMS = {
        'title': title,
        'asc': asc,
        'page': 1,
        'language': language,
        'fromDate': fromDate,
        'toDate': toDate,
        'tags': tags,
        'logicTag': logicTag
    }

    URL_FIRST = f"{reverse('repo_search_by_keys')}?{urlencode(URL_FIRST_PARAMS, True)}"


    start_delta = max(1, page - 2) - page

    for delta in range(start_delta, start_delta + 5):
        p = page + delta

        if p > 0 and (p - 1) * MAX_ITEMS_PER_PAGE < total_results:
            URL_PARAMS = {'title': title,
                          'asc': asc,
                          'page': p,
                          'language': language,
                          'fromDate': fromDate,
                          'toDate': toDate,
                          'tags': tags,
                          'logicTag': logicTag
                          }
            URL = f"{reverse('repo_search_by_keys')}?{urlencode(URL_PARAMS, True)}"
            URL_PAGES.append((p, p == page , URL))

    return render(request, 'code/search_by_keys.html', {
        'sources': sources,
        'URL_FLIP_CREATEDAT': URL_FLIP_CREATEDAT,
        'URL_PAGES': URL_PAGES,
        'asc': asc,
        'total_results': total_results,
        'URL_PREVIOUS': URL_PREVIOUS if page > 1 else False,
        'URL_NEXT': URL_NEXT if page * MAX_ITEMS_PER_PAGE < total_results else False,
        'URL_FIRST': URL_FIRST if len(URL_PAGES) and URL_PAGES[0][0] > 1 else None
    })

@require_http_methods(['GET', 'POST'])
def update(request, key):
    if request.method == 'GET':
        try:
            source = Code.objects.get(pk = key)
            tags = Tag.objects.all()
            tags_id = set(map(lambda tag: tag['id'], source.tags.values('id')))
            return render(request, 'code/update.html', {'source': source, 'tags': tags, 'tags_id': tags_id})
        except ObjectDoesNotExist as ex:
            return render(request, '404.html', {'message': ex})
    else:
        try:
            title = request.POST.get('title')
            original = request.POST.get('original')
            description = request.POST.get('description')
            tags = request.POST.getlist('tags')
            source = Code.objects.filter(pk = key).update(title = title, original = original, description = description, updatedAt = timezone.now())
            source = Code.objects.get(pk = key)
            source.tags.set(list(map(int, tags)))
            return redirect(reverse('repo_code_update', args = [key]))
        except ObjectDoesNotExist as ex:
            return render(request, '404.html', {'message': ex})

@require_http_methods(['POST'])
def delete(request, key):
    Code.objects.filter(pk = key).delete()
    return redirect(reverse('repo_inicio'))

@require_http_methods(['POST'])
def update_source(request, key):
    source = request.POST.get('source')
    language = request.POST.get('language')
    problem = Code.objects.filter(pk = key).update(source = source, language = language, updatedAt = timezone.now())
    return redirect(reverse('repo_code_view', args = [key]))
