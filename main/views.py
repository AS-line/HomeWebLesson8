from django.views.generic import ListView, DetailView
from .models import Article, Tag


class ArticleListView(ListView):
    template_name = "list.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_news"] = Article.objects.all()
        context["pages"] = Tag.objects.all()
        return context


class ArticleDetailView(DetailView):
    template_name = "detail.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new"] = Article.objects.get()
        context["pages"] = Tag.objects.all()
        return context
