from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import ArticleForm
from .models import Article
# Create your views here.


def article_search_view(request):
    query_dict = request.GET  # this is dictionary
    # query = query_dict.get("q")  # <input type="text" name="q" placeholder="Search" />

    try:
        query = int(query_dict.get("q"))
    except:  # ValueError should be near except
        query = None

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj
    }
    return render(request, 'articles/search.html', context=context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        # context['object'] = article_object
        # context['created'] = True
    return render(request, "articles/create.html", context=context)


# @login_required
# def article_create_view(request):
#     form = ArticleForm()
#     context = {
#         'form': form
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             article_object = Article.objects.create(title=title, content=content)
#             context['object'] = article_object
#             context['created'] = True
#     return render(request, "articles/create.html", context=context)


def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        # article_obj = Article.objects.get(slug=slug)
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()

    context = {
        'object': article_obj
    }
    return render(request, "articles/detail.html", context=context)
