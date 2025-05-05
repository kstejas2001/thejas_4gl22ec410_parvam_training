from django.urls import path
from . import views

urlpatterns = [
    # URLs for listing data
    path('students/', views.student_list, name='student_list'),
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='book_list'),

    # URLs for adding new entries
    path('add-student/', views.add_student, name='add_student'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-book/', views.add_book, name='add_book'),
]