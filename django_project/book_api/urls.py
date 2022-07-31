from django.contrib import admin
from django.urls import path
#from book_api.views import book, book_list, book_create
from book_api.views import BookList, BookCreate, Book_by_pk

urlpatterns = [
    # path('', book_create),
    # path('list/', book_list),
    # path('<int:pk>/',book)
    path('', BookCreate.as_view()),
    path('list/', BookList.as_view()),
    path('<int:pk>/',Book_by_pk.as_view())
]