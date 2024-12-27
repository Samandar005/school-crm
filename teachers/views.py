from django.shortcuts import render, redirect, get_object_or_404
from subjects.models import Subject
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teachers-list.html', ctx)

def teacher_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject_name = request.POST.get('subject')
        telephone_number = request.POST.get('telephone_number')
        email = request.POST.get('email')
        work_expert = request.POST.get('work_expert')
        if (
            image and first_name and last_name and subject_name and
                telephone_number and email and work_expert
        ):
            subject = Subject.objects.get(name=subject_name)
            Teacher.objects.create(
                image=image,
                first_name=first_name,
                last_name=last_name,
                subject=subject,
                telephone_number=telephone_number,
                email=email,
                work_expert=work_expert,
            )
            return redirect('teachers:list')
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'teachers/teacher-add.html', ctx)

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        image = request.FILES.get('image')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject_name = request.POST.get('subject')
        telephone_number = request.POST.get('telephone_number')
        email = request.POST.get('email')
        work_expert = request.POST.get('work_expert')
        if (
                image and first_name and last_name and subject_name and
                telephone_number and email and work_expert
        ):
            subject = Subject.objects.get(name=subject_name)
            teacher.image=image
            teacher.first_name=first_name
            teacher.last_name=last_name
            teacher.subject=subject
            teacher.telephone_number=telephone_number
            teacher.email=email
            teacher.work_expert=work_expert
            teacher.save()
            return redirect(teacher.get_detail_url())
    subjects = Subject.objects.all()
    ctx = {'teacher':teacher,
           'subjects': subjects,}
    return render(request, 'teachers/teacher-add.html', ctx)

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    ctx = {'teacher': teacher}
    return render(request, 'teachers/teacher-detail.html', ctx)

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    teacher.delete()
    return redirect('teachers:list')
