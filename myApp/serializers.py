
from .models import Employee , Courses , Instructor , Subjects
from rest_framework import serializers

# class EmployeeSerialzer(serializers.Serializer):
#     name = serializers.CharField(max_length= 50)
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=20)
#     phone = serializers.CharField(max_length= 20)

#     # this method is called before save data to the DB
#     def create(self, validated_data):
#         print("Create Method Called!")
#         return Employee.objects.create(**validated_data)

#     # this method is called before save data to the DB
#     def update(self, employee, validated_data):
#         print("Update existing employee!")
#         newEmp = Employee(**validated_data)
#         newEmp.id = employee.id
#         newEmp.save()
#         return newEmp

class EmployeeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class UserSerialzer(serializers.Serializer):
    username = serializers.CharField(max_length= 50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
    


class CourseSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'



class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'


class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    subjects = serializers.HyperlinkedRelatedField(many = True , read_only = True , view_name= 'subjects-detail')
    class Meta:
        model = Instructor
        fields = '__all__'