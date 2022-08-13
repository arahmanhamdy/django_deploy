import http
import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .models import Student
from .forms import StudentForm
from .serializers import StudentSerializer, UserSerializer
from .permissions import OwnStudentPermission


# Create your views here.

def all_students(request):
    students = Student.objects.all()
    return render(request, 'students/all_students.html', {'students': students})


def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail_student.html', {"student": student})


def edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('detail_student', student_id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/create_student.html', {'form': form})


def delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect('all_students')


def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('detail_student', student_id=student.id)
    else:
        form = StudentForm()
    return render(request, 'students/create_student.html', {'form': form})


@api_view(['GET', 'POST'])
def students_api(request):
    if request.method == "GET":
        students = Student.objects.all()
        serialized_students = StudentSerializer(students, many=True)
        return Response(serialized_students.data, status=http.HTTPStatus.OK)

    elif request.method == "POST":
        print(request.GET)
        student = StudentSerializer(data=request.data)
        if not student.is_valid():
            return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)
        student.save()
        return Response(student.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def student_api(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "GET":
        serialized_student = StudentSerializer(student)
        return Response(serialized_student.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        student = StudentSerializer(instance=student, data=request.data)
        if not student.is_valid():
            return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)
        student.save()
        return Response(student.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserApi(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


"""
GET /students   200
GET /students/<id>  200
POST /students  201
PUT /students/<id>  200
PATCH /students/<id> 200
DELETE /students/<id> 204 - 205
"""

"""
/students
/student/<pk>
"""

