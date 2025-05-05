from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Author, Book
from .forms import StudentForm, AuthorForm, BookForm

# View for listing all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'library_app/student_list.html', {'students': students})

# View for listing all authors
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library_app/author_list.html', {'authors': authors})

# View for listing all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library_app/book_list.html', {'books': books})

# View for adding a new student
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'library_app/add_student.html', {'form': form})

# View for adding a new author
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'library_app/add_author.html', {'form': form})

# View for adding a new book
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library_app/add_book.html', {'form': form})