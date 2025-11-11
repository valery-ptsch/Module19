import django_filters
from django import forms
from .models import Post
from django.contrib.auth.models import User


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название содержит'
    )

    author = django_filters.ModelChoiceFilter(
        field_name='author__user__username',
        queryset=User.objects.all(),
        label='Автор'
    )

    created_after = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='gte',
        label='Опубликовано после',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Post
        fields = ['title', 'author', 'created_after']