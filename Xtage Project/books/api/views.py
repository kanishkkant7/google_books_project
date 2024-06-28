from django.shortcuts import render,HttpResponse,redirect
from books.settings import BOOKS_API_KEY
import json
import requests
from django.http import JsonResponse,HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from collection.models import Book,Comment,Like,UserCollection

@csrf_exempt
def by_search(request):
    if request.method=="POST":
        base_url="https://www.googleapis.com/books/v1/volumes?q="
        data=json.loads(request.body)
        print(data)
        try:
            book_data=""
            url=base_url+data["data"]+"&key="+BOOKS_API_KEY
            print(url)
            response=requests.get(url)
            if response.status_code==200:
                book_data = response.json()
                request.session["session_data"]=book_data
                request.session["query"]=data["data"]
                request.session.save()
                print("Setting query in session:", data["data"])
                return redirect("display_books")
            else:
                book_data={"Failed to fetch book data":response.status_code}
                return JsonResponse({"status":200,"data":book_data})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        return HttpResponse("Error 400 : Bad Request")


def display_books(request):
    book_data = request.session.get("session_data")
    query=request.session.get("query")
    return render(request,"books/searchresults.html", {"book_data": book_data,"query":query}) 


def fetch_book_from_google_api(book_id):
    api_key = BOOKS_API_KEY
    url = f"https://www.googleapis.com/books/v1/volumes/{book_id}?key={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        volume_info = data.get('volumeInfo', {})
        
        return data
    return None

def book_details(request, book_id):
    book_data = request.session.get("book_session_data")
    session_book_id = request.session.get('book_session_bookId')
    
    print(f"This is book ID which was passed: {book_id}")
    print(f"This is book ID which was retrieved from session: {session_book_id}")
    
    if book_data and session_book_id == book_id:
        book = Book.objects.get(google_books_id=book_id)
    else:
        # Try to get book from database
        book = Book.objects.filter(google_books_id=book_id).first()
        
        if not book:
            # If not in database, fetch from Google API
            book_data = fetch_book_from_google_api(book_id)
            if book_data:
                # Save the fetched book to the database
                book = Book.objects.create(**book_data)
            else:
                return HttpResponseNotFound("Book not found in session, database, or Google API.")
        
        # Update session with new book data
        request.session["book_session_data"] = book.to_dict()  # Assume Book model has a to_dict method
        request.session["book_session_bookId"] = book_id

    comments = Comment.objects.filter(book=book).order_by('-created_at')
    liked = Like.objects.filter(user=request.user, book=book).exists()
    is_saved = UserCollection.objects.filter(user=request.user, book=book).exists()
    likes_count = book.likes.count()

    return render(request, 'books/book_details.html', {
        'book': book,
        'book_id': book_id,
        'comments': comments,
        'liked': liked,
        'is_saved': is_saved,
        'likes_count': likes_count
    })


@csrf_exempt
def by_id(request):
    if request.method=="POST":
        url = f'https://www.googleapis.com/books/v1/volumes/'
        data=json.loads(request.body)
        book_id=data["bookId"]
        url+=book_id
        response=requests.get(url)
        print(url)
        if response.status_code==200:
            request.session["book_session_data"]=response.json()
            request.session["book_session_bookId"]=book_id
            print(f"BY ID FUNCTION This is book ID which was passed: {book_id}")
            print(f"BY ID FUNCTION This is book ID which was saved in session: {request.session.get('book_session_bookId')}")
            return redirect("book_details",book_id=book_id)
    else:
        return HttpResponse("Error 400 : Bad Request")
