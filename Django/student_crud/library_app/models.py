from django.db import models

# Create Student models
class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=15, unique=True)
    branch = models.CharField(max_length=50)
    student_id  = models.IntegerField(unique=True) 
    email  = models.EmailField(max_length=100, blank=True, null=True) 
    phone  = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.usn})"
    
# Author  Model
class  Author(models.Model):
    name  = models.CharField(max_length=100)
    bio  = models.TextField(blank=True)
    dob = models.DateField(blank=True, null=True)
    nationality =  models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
    
#Book Model
class Book(models.Model):
    title =  models.CharField(max_length=150)
    book_id  =  models.CharField(max_length=20, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    available_copies = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} by {self.author.name}"