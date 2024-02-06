from django.urls import path
from .api.teacher_api import showAllTeachers,addTeachers,deleteTeacher,filterTeacher,updateTemplate,filteringTeacher

urlpatterns = [
    path("showteacher",showAllTeachers, name = "showAllTeachers", ),
    path("addteacher",addTeachers, name="addTeachers"),
    path("deleteteacher/<int:id>",deleteTeacher, name= "deleteTeachers"),
    path("update/<int:id>",updateTemplate,name = "UpdatingTemplates"),
    # path("updateteacher",updateTeacher,name= "updateTeachers"),
    # path("searchteacher",searchTeacher, name = "searchTeachers"),
    path("filterteacher",filterTeacher, name= "filterTeachers"),
    path("filtering",filteringTeacher, name= "filteringTeacher")
    # path("avgteacher",avergeClass)
]
