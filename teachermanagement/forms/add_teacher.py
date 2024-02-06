from ..model.teacher_model import Teacher
from django import forms



class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        labels = {
            "firstName": "First Name",
            "lastName": "Last Name",  # Fixed typo here
            "age": "Age",
            "dob": "Date Of Birth",
            "numberOfClass": "Number of Classes"
        }