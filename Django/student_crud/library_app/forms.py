from django import forms
from .models import Student, Author, Book

#form for Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

#Form for Author
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

#Form for Book
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'