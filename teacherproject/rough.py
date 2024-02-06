# from django.shortcuts import render
# from ..model.teacher_model import Teacher
# import json
# from datetime import date
# from django.http import HttpResponse
# from django.db.models import Count, Sum

# def date_encoder(obj):
#     if isinstance(obj, date):
#         return obj.strftime('%Y-%m-%d')
#     raise TypeError("Type error found")

# def showTeachers():
#     allTeachers = Teacher.objects.all()
#     return allTeachers
#     # listOfTeachers = []
#     # for teacher in allTeachers:
#     #         teacher_data = {
#     #             "firstName": teacher.firstName,
#     #             "lastName": teacher.lastName,
#     #             "age": teacher.age,
#     #             "dob": teacher.dob,
#     #             "numberOfClass": teacher.numberOfClass,
#     #         }
#     #         listOfTeachers.append(teacher_data)
#     # # Use json.dumps with custom encoder to serialize the data
#     # json_data = json.dumps(listOfTeachers, default=date_encoder)
#     # return json_data

# def addingNewTeacher(body):
#     teacher = json.loads(body)
#     firstName = teacher["firstName"]
#     lastName = teacher["lastName"]
#     age = teacher["age"]
#     dob = teacher["dob"]
#     numberOfClass = teacher["numberOfClass"]
#     teacher = Teacher(firstName=firstName,lastName=lastName,age=age,dob = dob,numberOfClass = numberOfClass)
#     teacher.save() 

# def deletingTeacher(id):
#     teacher = Teacher.objects.get(id =id)
#     teacher.delete()

# def updatingTeacherInfo(body):
#         teacher_detail = json.loads(body)
#         print(teacher_detail)
#         teacher_id = teacher_detail.get("id")
#         print(teacher_id)
        
#         try:
#             teacher = Teacher.objects.get(id=teacher_id)
#         except Exception as E:
#             return HttpResponse("Teacher not found", status=404)

#         if "firstName" in teacher_detail:
#             teacher.firstName = teacher_detail["firstName"]
#         if "lastName" in teacher_detail:
#             teacher.lastName = teacher_detail["lastName"]
#         if "age" in teacher_detail:
#             teacher.age = teacher_detail["age"]
#         if "dob" in teacher_detail:
#             teacher.dob = teacher_detail["dob"]
#         if "numberOfClass" in teacher_detail:
#             teacher.numberOfClass = teacher_detail["numberOfClass"]
#         teacher.save()
        
        
# def searchingTeacher(name):    
#     teacher = Teacher.objects.filter(firstName__icontains = name)
#     if teacher:
#         listOfTeachers = []
#         for teacher in teacher:
#             teacher_data = {
#                 "firstName": teacher.firstName,
#                 "lastName": teacher.lastName,
#                 "age": teacher.age,
#                 "dob": teacher.dob,
#                 "numberOfClass": teacher.numberOfClass,
#             }
#             listOfTeachers.append(teacher_data)
#     # Use json.dumps with custom encoder to serialize the data
#         json_data = json.dumps(listOfTeachers, default=date_encoder)
#         return json_data
#     else:
#         return 0
    
    
# def filtering(age,numberOfClass):
#     if(age != " " and numberOfClass != " "):
#         teacher = Teacher.objects.filter(age = age, numberOfClass = numberOfClass)
#         if teacher:
#             listOfTeachers = []
#         for teacher in teacher:
#             teacher_data = {
#                 "firstName": teacher.firstName,
#                 "lastName": teacher.lastName,
#                 "age": teacher.age,
#                 "dob": teacher.dob,
#                 "numberOfClass": teacher.numberOfClass,
#             }
#             listOfTeachers.append(teacher_data)
#     # Use json.dumps with custom encoder to serialize the data
#             json_data = json.dumps(listOfTeachers, default=date_encoder)
#             return json_data
#         else:
#             return 0
#     elif(age != " "):
#         teacher = Teacher.objects.filter(age = age)
#         if teacher:
#             listOfTeachers = []
#         for teacher in teacher:
#             teacher_data = {
#                 "firstName": teacher.firstName,
#                 "lastName": teacher.lastName,
#                 "age": teacher.age,
#                 "dob": teacher.dob,
#                 "numberOfClass": teacher.numberOfClass,
#             }
#             listOfTeachers.append(teacher_data)
#     # Use json.dumps with custom encoder to serialize the data
#             json_data = json.dumps(listOfTeachers, default=date_encoder)
#             return json_data
#         else:
#             return 0
#     else:
#         teacher = Teacher.objects.filter(numberOfClass = numberOfClass)
#         if teacher:
#             listOfTeachers = []
#         for teacher in teacher:
#             teacher_data = {
#                 "firstName": teacher.firstName,
#                 "lastName": teacher.lastName,
#                 "age": teacher.age,
#                 "dob": teacher.dob,
#                 "numberOfClass": teacher.numberOfClass,
#             }
#             listOfTeachers.append(teacher_data)
#         # Use json.dumps with custom encoder to serialize the data
#             json_data = json.dumps(listOfTeachers, default=date_encoder)
#             return json_data
#         else:
#             return 0
        

# def avergeClass(id):
#     total_number_of_class = Teacher.objects.all().aaggregate(total_number_teachers = Sum("numberOfClass"))
#     print(total_number_of_class)
#     teacher = Teacher.objects.get(id = id)
#     teacher_class = teacher.numberOfClass
#     return teacher_class / total_number_of_class
    
            

    