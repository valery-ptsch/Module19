# Импорт моделей
from django.contrib.auth.models import User
from news.models import Author, Category, Post, PostCategory, Comment

print("=== 1. Создание пользователей ===")
user1 = User.objects.create_user('user1', password='testpass123')
user2 = User.objects.create_user('user2', password='testpass123')
print(f"Созданы пользователи: {user1.username}, {user2.username}")

print("\n=== 2. Создание авторов ===")
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)
print(f"Созданы авторы: {author1.user.username}, {author2.user.username}")

print("\n=== 3. Добавление категорий ===")
category1 = Category.objects.create(name='Спорт')
category2 = Category.objects.create(name='Политика')
category3 = Category.objects.create(name='Образование')
category4 = Category.objects.create(name='Технологии')
print(f"Созданы категории: {category1.name}, {category2.name}, {category3.name}, {category4.name}")

print("\n=== 4. Добавление статей и новостей ===")
post1 = Post.objects.create(
    author=author1,
    post_type=Post.ARTICLE,
    title='Первая статья о спорте',
    content='Это содержимое первой статьи о спорте. ' * 10
)
post2 = Post.objects.create(
    author=author2,
    post_type=Post.ARTICLE,
    title='Вторая статья о политике',
    content='Это содержимое второй статьи о политике. ' * 10
)
post3 = Post.objects.create(
    author=author1,
    post_type=Post.NEWS,
    title='Новость об образовании и редисках',
    content='Это новость об образовании с упоминанием редисок и негодяев. ' * 10
)
print(f"Созданы посты: {post1.title}, {post2.title}, {post3.title}")

print("\n=== 5. Присвоение категорий ===")
PostCategory.objects.create(post=post1, category=category1)
PostCategory.objects.create(post=post1, category=category2)
PostCategory.objects.create(post=post2, category=category2)
PostCategory.objects.create(post=post2, category=category3)
PostCategory.objects.create(post=post3, category=category3)
PostCategory.objects.create(post=post3, category=category4)
print("Категории присвоены постам")

print("\n=== 6. Создание комментариев ===")
comment1 = Comment.objects.create(post=post1, user=user1, text='Отличная статья о спорте!')
comment2 = Comment.objects.create(post=post1, user=user2, text='Интересная точка зрения')
comment3 = Comment.objects.create(post=post2, user=user1, text='Согласен с автором')
comment4 = Comment.objects.create(post=post3, user=user2, text='Важная новость для образования')
print("Создано 4 комментария")

print("\n=== 7. Корректировка рейтингов через like/dislike ===")
post1.like()
post1.like()
post1.like()
post1.dislike()
print(f"Рейтинг post1: {post1.rating}")

post2.like()
post2.like()
post2.like()
post2.like()
post2.like()
print(f"Рейтинг post2: {post2.rating}")

post3.dislike()
post3.dislike()
print(f"Рейтинг post3: {post3.rating}")

comment1.like()
comment1.like()
comment1.like()
comment1.like()
comment2.dislike()
comment3.like()
comment3.like()
comment4.dislike()
comment4.dislike()

print("Рейтинги комментариев:")
for i, comment in enumerate([comment1, comment2, comment3, comment4], 1):
    print(f"Комментарий {i}: {comment.rating}")

print("\n=== 8. Обновление рейтингов пользователей ===")
author1.update_rating()
author2.update_rating()
print(f"Рейтинг author1: {author1.rating}")
print(f"Рейтинг author2: {author2.rating}")

print("\n=== 9. Лучший пользователь ===")
best_author = Author.objects.order_by('-rating').first()
print(f"Лучший пользователь: {best_author.user.username} с рейтингом {best_author.rating}")

print("\n=== 10. Лучшая статья ===")
best_post = Post.objects.order_by('-rating').first()
print(f"Дата добавления: {best_post.created_at}")
print(f"Автор: {best_post.author.user.username}")
print(f"Рейтинг: {best_post.rating}")
print(f"Заголовок: {best_post.title}")
print(f"Превью: {best_post.preview()}")

print("\n=== 11. Комментарии к лучшей статье ===")
comments = Comment.objects.filter(post=best_post)
print(f"Всего комментариев: {comments.count()}")
for comment in comments:
    print(f"Дата: {comment.created_at}, Пользователь: {comment.user.username}, Рейтинг: {comment.rating}, Текст: {comment.text}")