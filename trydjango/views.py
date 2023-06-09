import random

from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request, *args, **kwargs):
    name = 'Jusin'
    random_id = random.randint(1, 4)

    # from the database ??

    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    context = {
        'object_list': article_queryset,
        'object': article_obj,
        'title': article_obj.title,
        'content': article_obj.content,
        'id': article_obj.id
    }
    HTML_STRING = render_to_string("home-view.html", context=context)
    return HttpResponse(HTML_STRING)
