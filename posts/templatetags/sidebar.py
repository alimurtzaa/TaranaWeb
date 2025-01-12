from django.template import Library
from ..models import Post, Comment
from django.db.models import Count

register = Library()

@register.inclusion_tag('includes/sidebar.html')
def sidebar_view(user=None):
    top_posts = Post.objects.annotate(num_likes=Count('likes')).filter(num_likes__gt=0).order_by("-num_likes")
    top_comments = Comment.objects.annotate(num_likes=Count('likes')).filter(num_likes__gt=0).order_by("-num_likes")
    context = {
        'top_posts': top_posts,
        'top_comments': top_comments,
        'user': user
    }
    return context