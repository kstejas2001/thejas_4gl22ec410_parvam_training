from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher
from .forms import TeacherForm
from django.contrib import messages

# Create your views here.
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_crud/teacher_list.html', {'teachers': teachers})

def create_teacher(request):
    # teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=Teacher)
        if form.is_valid():
            form.save()
            messages.success(request, 'Teacher updated successfully!')
            return redirect('teacher_list')
        else:
            messages.error(request, 'Error updating teacher. Please check the form.')
    else:
        form = TeacherForm(instance=Teacher)
    
    return render(request, 'teacher_crud/create_teacher.html', {'form': form, 'update': True, 'teacher': Teacher})

def view_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teacher_crud/view_teacher.html', {'teacher': teacher})

def edit_teacher(request):
    return render(request, 'teacher_crud/edit_teacher.html')

def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return render(request, 'teacher_crud/delete_teacher.html')
