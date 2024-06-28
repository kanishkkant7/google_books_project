from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Book, Comment, Like, UserCollection
from django.views.decorators.csrf import csrf_exempt


@login_required
@require_POST
def like_book(request, book_id):
    book = get_object_or_404(Book, google_books_id=book_id)
    liked = Like.objects.filter(user=request.user, book=book).exists()
    if liked:
        Like.objects.filter(user=request.user, book=book).delete()
        liked = False
    else:
        Like.objects.create(user=request.user, book=book)
        liked = True
    likes_count = book.likes.count()  # Ensure to always fetch the updated count
    return JsonResponse({'liked': liked, 'likes_count': likes_count})




@login_required
@require_POST
def add_comment(request, book_id):
    book = get_object_or_404(Book, google_books_id=book_id)
    text = request.POST.get('text')
    if text:
        comment = Comment.objects.create(user=request.user, book=book, text=text)
        return JsonResponse({
            'comment': {
                'text': comment.text,
                'timestamp': comment.created_at.strftime('%Y-%m-%d %H:%M'),
                'user': comment.user.username
            }
        })
    return JsonResponse({'error': 'No text provided'}, status=400)


@login_required
@require_POST
def save_book(request, book_id):
    book_data = request.session.get("book_session_data")
    if book_data:
        book, created = Book.objects.get_or_create(
            google_books_id=book_data['id'],
            defaults={
                'title': book_data['volumeInfo']['title'],
                'authors': ', '.join(book_data['volumeInfo'].get('authors', [])),
                'thumbnail_url': book_data['volumeInfo']['imageLinks'].get('thumbnail')
            }
        )
        user_collection, created = UserCollection.objects.get_or_create(user=request.user, book=book)
        if not created:
            user_collection.delete()
            saved = False
        else:
            saved = True
        return JsonResponse({'saved': saved})
    return JsonResponse({'error': 'Book data not found in session'}, status=400)
