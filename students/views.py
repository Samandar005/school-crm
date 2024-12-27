from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Group


def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/students-list.html', ctx)

def student_create(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        group = request.POST.get('group')
        date_of_birth = request.POST.get('date_of_birth')
        telephone_number = request.POST.get('telephone_number')
        address = request.POST.get('address')
        if image and first_name and last_name and date_of_birth and telephone_number and address:
            group = Group.objects.get(group_name=group)
            Student.objects.create(
                image=image,
                first_name=first_name,
                last_name=last_name,
                group=group,
                date_of_birth=date_of_birth,
                telephone_number=telephone_number,
                address=address,
            )
            return redirect('students:list')
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'students/student-add.html', ctx )

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        image = request.FILES.get('image')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        group_name = request.POST.get('group')
        date_of_birth = request.POST.get('date_of_birth')
        telephone_number = request.POST.get('telephone_number')
        address = request.POST.get('address')
        if image and first_name and last_name and date_of_birth and telephone_number and address:
            group = Group.objects.get(group_name=group_name)
            student.image=image
            student.first_name=first_name
            student.last_name=last_name
            student.group=group
            student.date_of_birth=date_of_birth
            student.telephone_number=telephone_number
            student.address=address
            student.save()
            return redirect(student.get_detail_url())
    groups = Group.objects.all()
    ctx = {
            'student': student,
            'groups': groups,
           }
    return render(request, 'students/student-add.html', ctx)

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    ctx = {'student': student}
    return render(request, 'students/student-detail.html', ctx)

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('students:list')


