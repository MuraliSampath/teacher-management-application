from django.shortcuts import render
from ..model.teacher_model import Teacher
import json
from datetime import date
from django.http import HttpResponse
from django.db.models import Count, Sum
from django.db.models import Q

def date_encoder(obj):
    if isinstance(obj, date):
        return obj.strftime('%Y-%m-%d')
    raise TypeError("Type error found")

def Average(teachers):
    total_count = 0
    total_avg = 0
    for i in teachers:
        total_count = total_count + 1
        total_avg = total_avg + i.numberOfClass
    Avg = total_avg / total_count
    return Avg

def showTeachers():
    allTeachers = Teacher.objects.all()
    return allTeachers
    

def deletingTeacher(id):
    teacher = Teacher.objects.get(id =id)
    teacher.delete()

def updatingTeacherInfo(teachers,id):
        teacher_detail = teachers
        teacher_id = id
        teacher = Teacher.objects.get(id=teacher_id)
        teacher.firstName = teacher_detail["firstName"]
        teacher.lastName = teacher_detail["lastName"]
        teacher.age = teacher_detail["age"]
        teacher.dob = teacher_detail["dob"]
        teacher.numberOfClass = teacher_detail["numberOfClass"]
        teacher.save()
                
def searchingTeacher(name):    
    teacher = Teacher.objects.filter(Q(firstName__istartswith=name) | Q(firstName__istartswith=name))
    
    if teacher:
        return teacher
    else:
        return 0

def searchingTeacherAllFilters(name,age,numberOfClass):    
    teacher = Teacher.objects.filter(firstName__icontains = name).filter(age = age).filter(numberOfClass = numberOfClass)
    if teacher:
        return teacher
    else:
        return 0
    
    
def filtering(age,numberOfClass):
    if(age  and numberOfClass ):
        teacher = Teacher.objects.filter(age = age, numberOfClass = numberOfClass)
        if teacher:
            return teacher
        else:
            return 0
    elif(age ):
        teacher = Teacher.objects.filter(age = age)
        if teacher:
            return teacher
        else:
            return 0
    else:
        teacher = Teacher.objects.filter(numberOfClass = numberOfClass)
        if teacher:
            return teacher
        else:
            return 0
        

    
            

    