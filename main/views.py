from django.views.generic import ListView, DetailView, TemplateView
from .models import Article, Tag


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pages"] = Tag.objects.all()
        return context


class ArticleListView(ListView):
    template_name = "list.html"
    model = Article
    paginate_by = 3
    context_object_name = "all_news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pages"] = Tag.objects.all()
        return context


class ArticleDetailView(DetailView):
    template_name = "detail.html"
    model = Article
    context_object_name = "new"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pages"] = Tag.objects.all()
        return context
