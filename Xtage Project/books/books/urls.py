from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path,include
from . import views as books
from api.views import *
from accounts import views as auth
from collection import views as coll
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",books.homepage,name="homepage"),
    path("search/",books.searchpage,name="searchpage"),
    path("api/search",by_search,name="by_search"),
    path("search/show_results",display_books,name="display_books"),
    path("login/",auth.loginView.as_view(),name="login"),
    path('register/', auth.RegisterView.as_view(), name='register'),
    path('profile/', books.user_profile, name='user_profile'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
    path('api/by_id', by_id, name='by_id'),
    path('book_details/<slug:book_id>/', book_details, name='book_details'),
    path('collection/like/<str:book_id>/', coll.like_book, name='like_book'),
    path('collection/comment/<str:book_id>/', coll.add_comment, name='add_comment'),
    path('collection/save/<str:book_id>/', coll.save_book, name='save_book'),

]
