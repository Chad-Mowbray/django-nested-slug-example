from django.shortcuts import render, redirect, HttpResponse
from .models import Cohort, Student
from .forms import CohortForm, StudentForm

def get_cohort(cohort_uuid):
    return Cohort.objects.get(id=cohort_uuid)

def cohort_list(request):
    cohorts = Cohort.objects.all()
    return render(request, 'cohorts_and_students/cohorts_list.html', {'cohorts': cohorts})

def cohort_detail(request, cohort_uuid):
    cohort = get_cohort(cohort_uuid)
    return render(request, 'cohorts_and_students/cohort_detail.html', {'cohort': cohort})

def new_cohort(request):
    if request.method == "POST":
        form = CohortForm(request.POST)
        if form.is_valid():
            cohort = form.save(commit=False)
            cohort.save()
            return redirect('cohort_detail', cohort_uuid=cohort.uuid)
    else:
        form = CohortForm()
    return render(request, 'cohorts_and_students/cohort_form.html', {'form': form, 'type_of_request': 'New'})

def edit_cohort(request, cohort_uuid):
    cohort = get_cohort(cohort_uuid)
    if request.method == "POST":
        form = CohortForm(request.POST, instance=cohort)
        if form.is_valid():
            cohort = form.save(commit=False)
            cohort.save()
            return redirect('cohort_detail', cohort_uuid=cohort.uuid)
    else:
        form = CohortForm(instance=cohort)
    return render(request, 'cohorts/cohort_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_cohort(request, cohort_uuid):
    if request.method == "POST":
        cohort = get_cohort(cohort_uuid)  
        cohort.delete()
    return redirect('cohort_list')



def get_student(student_slug):
    return Student.objects.get(slug=student_slug)

def student_list(request, cohort_uuid):
    cohort = get_cohort(cohort_uuid)
    students = cohort.students.all()
    return render(request, 'cohorts_and_students/students_list.html', {'cohort': cohort, 'students': students})

def student_detail(request, cohort_uuid, student_slug):
    cohort = get_cohort(cohort_uuid)
    student = get_student(student_slug)
    return render(request, 'cohorts_and_students/student_detail.html', {'cohort': cohort, 'student': student})

def new_student(request, cohort_uuid):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', cohort_uuid=student.cohort.uuid, student_slug=student.slug)
    else:
        form = StudentForm()
    return render(request, 'cohorts_and_students/student_form.html', {'form': form, 'type_of_request': 'New'})

def edit_student(request, cohort_uuid, student_slug):
    cohort = get_cohort(cohort_uuid)
    student = get_student(student_slug)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('student_detail', student_slug=student.slug, cohort_uuid=cohort_uuid)
    else:
        form = StudentForm(instance=student)
    return render(request, 'cohorts_and_students/student_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_student(request, cohort_uuid, student_slug):
    if request.method == "POST":
        student = get_student(student_slug)
        student.delete()
    return redirect('student_list', cohort_uuid=cohort_uuid)