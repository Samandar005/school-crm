from django.shortcuts import render, redirect, get_object_or_404
from .models import Group, Teacher


def home(request):
    return render(request, 'index.html')

def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/groups-list.html', ctx)

def group_create(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        teachers = request.POST.get('teachers')
        students = request.POST.get('students')
        if group_name and students and teachers:
            Group.objects.create(
                group_name = group_name,
                teachers = teachers,
                students=students,
            )
            return redirect('groups:list')
    return render(request, 'groups/group-add.html', )

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














