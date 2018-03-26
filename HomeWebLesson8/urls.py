from django.contrib import admin
from django.urls import path, include
from main.views import ArticleDetailView, ArticleListView, HomeView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name="home"),
    path("news/", ArticleListView.as_view(), name='list'),
    path("news/<slug:slug>", ArticleDetailView.as_view(), name='detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
