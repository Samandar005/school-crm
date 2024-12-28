from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from teachers.models import Teacher
from students.models import Student
from subjects.models import Subject


def home(request):
    ctx = {
        'teachers_count': Teacher.objects.count(),
        'groups_count': Group.objects.count(),
        'students_count': Student.objects.count(),
        'subjects_count': Subject.objects.count(),
    }
    return render(request, 'index.html', ctx)

def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/groups-list.html', ctx)

def group_create(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        teacher_id = request.POST.get('teachers')
        students = request.POST.get('students')
        if group_name and students and teacher_id:
            teacher = Teacher.objects.get(id=teacher_id)
            Group.objects.create(
                group_name = group_name,
                teachers = teacher,
                students=students,
            )
            return redirect('groups:list')
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'groups/group-add.html', ctx)

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        teachers = request.POST.get('teachers')
        students = request.POST.get('students')
        if group_name and students and teachers:
            group.group_name=group_name
            group.teachers=teachers
            group.students=students
            group.save()
            return redirect(group.get_detail_url())
    ctx = {'group': group}
    return render(request, 'groups/group-add.html', ctx)

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group': group}
    return render(request, 'groups/group-detail.html', ctx)

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('groups:list')














