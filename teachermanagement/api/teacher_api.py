from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Importing the Models
from ..model.teacher_model import Teacher
import json
from django.http import HttpResponse

#Importing the Forms
from ..forms.add_teacher import TeacherForm

#Importing Services
from ..service.teacher import showTeachers,deletingTeacher,updatingTeacherInfo,searchingTeacher,filtering,searchingTeacherAllFilters,Average


def showAllTeachers(request):
        teachers = showTeachers() # Assuming showTeachers() returns a queryset of Teacher objects
        avg = Average(teachers)
        
        return render(request,"teachermanagement/show_teacher.html",{
            "teachers":teachers, "title":"Show All Teacher", "avg":avg
        })
        
def addTeachers(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()  # Save the form data to the database or perform other actions
            return HttpResponseRedirect("showteacher")
        else:
            print(form.errors)
    else:
        teacherForm = TeacherForm()
        return render(request, "teachermanagement/add_teacher.html", {
        "form": teacherForm
    })

def deleteTeacher(request,id):
    try:
        print(id)
        deletingTeacher(id)
        return HttpResponseRedirect("/teacher/showteacher")
    except:
        return HttpResponseBadRequest("ID is Not Found")
        
def updateTemplate(request,id):
    if request.method == "GET":
        teacher = Teacher.objects.get(id = id)
        form = TeacherForm(instance= teacher)
        return render(request, "teachermanagement/update_teacher.html", {
        "form": form,"id":id
    })
    
    elif request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(cleaned_data)
            print(id)
            # print(cleaned_data["firstName"])
            updatingTeacherInfo(cleaned_data,id)
            return HttpResponseRedirect("/teacher/showteacher")


def filterTeacher(request):
        age = request.GET.get("age"," ")
        numberOfClass = request.GET.get("numberOfClass"," ")
        ListOfTeachers = filtering(age = age, numberOfClass = numberOfClass)
        if(ListOfTeachers != 0):
            return HttpResponse(ListOfTeachers)
        else:
            return HttpResponse("No Records Found")
        
        
def filteringTeacher(request):
    if request.method == "GET":
        return render(request, "teachermanagement/filter_teacher.html")
    elif request.method == "POST":
        search_name = request.POST.get('searchName')
        age = request.POST.get('age')
        number_of_class = request.POST.get('numberOfClass')
       
        
        if(search_name and age and number_of_class):
            teacherList = searchingTeacherAllFilters(search_name,age,number_of_class)
            return render(request, "teachermanagement/filter_teacher.html", {"teachers": teacherList})
        elif search_name:
            teacherList = searchingTeacher(search_name)
            return render(request, "teachermanagement/filter_teacher.html", {"teachers": teacherList})
        elif (age and number_of_class) or age or number_of_class:
            teacherList = filtering(age, number_of_class)
            return render(request, "teachermanagement/filter_teacher.html", {"teachers": teacherList})

            
