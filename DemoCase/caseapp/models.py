from django.db import models
from tinymce.models import HTMLField

'fan520'


class Path(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "阶段"
        verbose_name_plural = verbose_name


class Case(models.Model):
    title = models.CharField('考试题', max_length=120)
    answer = HTMLField()
    path = models.ForeignKey(Path, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "试题"
        verbose_name_plural = verbose_name
