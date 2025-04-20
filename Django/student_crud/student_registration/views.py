from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from .models import Registration


# Create your views here.
def registration_list(request):
    students = Registration.objects.all()
    return render(request, "student_registration/registration_list.html", {'students': students})

def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = RegistrationForm()
    return render(request, "student_registration/registration_form.html", {'form': form})

def view_registration(request, pk):
    student = get_object_or_404(Registration, pk=pk)
    return render(request, "student_registration/view_registration.html", {'student': student})

def update_registration(request, pk):
    student = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = RegistrationForm(instance=student)
    return render(request, "student_registration/registration_form.html", {'form': form})

def delete_registration(request, pk):
    student = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    return render(request, "student_registration/delete_registration.html", {'student': student})