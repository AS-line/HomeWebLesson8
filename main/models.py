from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Tag(models.Model):
    title = models.CharField("Название тега", max_length=50)
    slug = models.SlugField(max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Article(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    slug = models.SlugField(max_length=32)
    date = models.DateField("Дата", default=timezone.now)
    img = models.ImageField("Изображение", upload_to="images", blank=True, null=True)
    content = RichTextUploadingField('Контент')
    tags = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def get_img_url(self):
        if self.img:
            return self.img.url
        return ''

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
