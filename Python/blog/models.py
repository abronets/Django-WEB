from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"

    def __str__(self):
        return "Title : {}. Author : {}".format(self.title, self.author)


class Comment(models.Model):
    text = models.TextField(_('Текст поста'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Автор'),
                             on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name=_('Пост'))
    created_datetime = models.DateTimeField(_('Дата і час створення'), auto_now_add=True)
    edited_datetime = models.DateTimeField(_('Дата і час редагування'), auto_now=True)

    def __str__(self):
        return '{0} - Пост № {1}'.format(self.user.email, self.post.id)

    class Meta:
        verbose_name = _('Коментарій')
        verbose_name_plural = _('Коментарії')
