from random import randint

from django import template
from django.template.loader import render_to_string

from ..models import Post

register = template.Library()


@register.simple_tag()
def random_post():
    while True:
        random_id = randint(Post.objects.first().id, Post.objects.last().id)
        if Post.objects.filter(id=random_id).exists():
            return render_to_string(
                    'blog/include/random_post.html',
                    {
                        'random_post': Post.objects.get(id=random_id),
                        'id': random_id
                    }

                )