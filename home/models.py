from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='image')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    type = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    image = models.ImageField(upload_to='image')
    detail = RichTextUploadingField()
    add_time = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'News'

    def image_post(self):
        return format_html('<img src="/mymedia/{}" alt="img" style="width:40px;height:40px;"  />'.format(self.image))

    def __str__(self):
        return self.title
