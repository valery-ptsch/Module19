from django.shortcuts import render, get_object_or_404
from .models import Post

def news_list(request):
    # Получаем только новости (не статьи), отсортированные от новых к старым
    news = Post.objects.filter(post_type=Post.NEWS).order_by('-created_at')
    return render(request, 'news/news_list.html', {'news_list': news})

def news_detail(request, pk):
    news = get_object_or_404(Post, pk=pk, post_type=Post.NEWS)
    return render(request, 'news/news_detail.html', {'news': news})