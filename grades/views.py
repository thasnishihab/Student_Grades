from django.shortcuts import render

# Create your views here.
from .models import Student, Subject
from django.db.models import Q


# def student_

def student_list(request):
    # import pdb
    # pdb.set_trace()
    query = request.GET.get('q')
    filter_remarks = request.GET.get('remarks')

    students = Student.objects.all().order_by('student_name')
    if query:
        students = students.filter(student_name=query)
    if filter_remarks:
        students = students.filter(remarks=filter_remarks)

    return render(request, 'grades/student_list.html', {'students': students})
