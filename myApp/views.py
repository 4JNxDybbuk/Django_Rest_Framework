import imp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, Courses , Instructor , Subjects
from .serializers import EmployeeSerialzer, UserSerialzer, CourseSerialzer , InstructorSerializer , SubjectSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet , ModelViewSet

# to get all employee details and also add employee to the DB.
# the following decorator is used for ignoring csrf token middlewares.

# @ csrf_exempt
# def employeeDashboard(request):
#     if request.method == 'POST':
#         # to convert JSON data to python dictionary
#         empJsonData = JSONParser().parse(request)
#         employeeJSON = EmployeeSerialzer(data= empJsonData)

#         # to check the data is valid or not
#         if employeeJSON.is_valid():
#             # save data to the DB
#             employeeJSON.save()
#             return JsonResponse(employeeJSON.data , safe= False)
#         else:
#             return JsonResponse(employeeJSON.errors , safe= False)
#     else:
#         employee = Employee.objects.all()
#         employeeJSON = EmployeeSerialzer(employee , many = True)
#         return JsonResponse(employeeJSON.data , safe= False)


# to get all user details from DB
# if you don't use safe keyword then you will pass data as dictionary format.
def userDashboard(request):
    user = User.objects.all()
    userJSON = UserSerialzer(user, many=True)
    return JsonResponse({"users": userJSON.data})


# to perform operation on Employee table like get emp by id , update emp & delete emp by id.

# @ csrf_exempt
# def employeeDetails(request , id):

#     # using try-except for checking id of emp is exist or not.
#     try:
#         employee = Employee.objects.get(pk = id)
#     except Employee.DoesNotExist:
#         return JsonResponse({ 'message': 'Sorry Employee Does Not Exist!!'} , status = 401)


#     if request.method == 'GET':
#         serializer = EmployeeSerialzer(employee)
#         return JsonResponse(serializer.data , safe= False)

#     elif request.method == 'PUT':
#         # to convert JSON data to python dictionary
#         employeeJsonData = JSONParser().parse(request)
#         serializer = EmployeeSerialzer(employee , data= employeeJsonData)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data , safe= False , status = 200)
#         else:
#             return JsonResponse(serializer.errors , safe= False , status = 401)

#     elif request.method == 'DELETE':
#         employee.delete()
#         return JsonResponse({ 'message': 'Employee id = {} has been deleted!!'.format(id) } , status = 200)


# to get all employee details and also add employee to the DB.
# Response object works like a JsonResponse object.

@api_view(['POST', 'GET'])
def employeeDashboard(request):
    if request.method == 'POST':
        employeeJSON = EmployeeSerialzer(data=request.data)

        # to check the data is valid or not
        if employeeJSON.is_valid():
            # save data to the DB
            employeeJSON.save()
            return Response(employeeJSON.data, status=200)
        else:
            return Response(employeeJSON.errors,  status=401)
    else:
        employee = Employee.objects.all()
        employeeJSON = EmployeeSerialzer(employee, many=True)
        return Response(employeeJSON.data)


# to perform operation on Employee table like get emp by id , update emp & delete emp by id.
@api_view(['GET', 'PUT', 'DELETE'])
def employeeDetails(request, id):

    # using try-except for checking id of emp is exist or not.
    try:
        employee = Employee.objects.get(pk=id)
    except Employee.DoesNotExist:
        return Response({'message': 'Sorry Employee Does Not Exist!!'}, status=401)

    if request.method == 'GET':
        serializer = EmployeeSerialzer(employee)
        return Response(serializer.data, status=200)

    elif request.method == 'PUT':
        serializer = EmployeeSerialzer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=200)
        else:
            return Response(serializer.errors,  status=401)

    elif request.method == 'DELETE':
        employee.delete()
        return Response({'message': 'Employee id = {} has been deleted!!'.format(id)}, status=200)


# to handle HTTP GET & POST request.
# @api_view(['GET', 'POST'])
# def courseDashboard(request):
#     if request.method == 'GET':
#         allCourse = Courses.objects.all()
#         serialzer = CourseSerialzer(allCourse, many=True)
#         return Response(serialzer.data, status=200)
#     elif request.method == 'POST':
#         serialzer = CourseSerialzer(data=request.data)

#         if serialzer.is_valid():
#             serialzer.save()
#             return Response(serialzer.data, status=200)
#         else:
#             return Response(serialzer.errors, status=401)


# to handle HTTP GET , PUT , DELETE request.
# @api_view(['GET', 'PUT', 'DELETE'])
# def courseDetails(request, id):

#     try:
#         course = Courses.objects.get(pk=id)
#     except Courses.DoesNotExist:
#         return Response({"message": "Course Not Found"}, status=401)

#     if request.method == 'GET':
#         serializer = CourseSerialzer(course)
#         return Response(serializer.data, status=200)

#     elif request.method == 'PUT':
#         serializer = CourseSerialzer(course, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         else:
#             return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
        # course.delete()
        # return Response({"message": "Course id {}has been deleted".format(id)}, status=200)


# Create class based view for courses..
# APIView is a class which is help us to handle HTTP GET , PUT , POST , DELETE , PATCH requset

'''
class CourseLists(APIView):

    # it handles HTTP GET request..
    def get(self, request):
        allCourse = Courses.objects.all()
        serialzer = CourseSerialzer(allCourse, many=True)
        return Response(serialzer.data, status=200)

    # it handles HTTP POST request..
    def post(self, request):
        serialzer = CourseSerialzer(data=request.data)

        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status=200)
        else:
            return Response(serialzer.errors, status=401)


class CourseModification(APIView):

    # get course bt id.
    def get_course(self, id):
        try:
            return Courses.objects.get(pk=id)
        except Courses.DoesNotExist:
            raise Http404
       
    
    # it handles HTTP GET request..
    def get(self, request, id):
        course = self.get_course(id)
        serializer = CourseSerialzer(course)
        return Response(serializer.data, status=200)

    
    # it handles HTTP PUT request..
    def put(self , request , id):
        course = self.get_course(id)
        serializer = CourseSerialzer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    
    # it handles HTTP DELETE request..
    def delete(self , request , id):
        course = self.get_course(id)
        course.delete()
        return Response({"message": "Course id {} has been deleted".format(id)}, status=200)

'''

# Mixin Example for the class based view

'''
class CourseLists(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerialzer

    # it handles HTTP GET request from GenericAPIView.. & list() used from ListModelMixin
    def get(self , request):
        return self.list(request)

    # it handles HTTP POST request from GenericAPIView..& create() used from CreateModelMixin
    def post(self , request):
        return self.create(request)


class CourseModification(generics.GenericAPIView , mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin):
    queryset = Courses.objects.all()
    serializer_class = CourseSerialzer
    
    # it handles HTTP GET request from GenericAPIView.. & retrieve() used from RetrieveModelMixin
    def get(self , request , pk):
        return self.retrieve(request , pk)
    
    # it handles HTTP PUT request from GenericAPIView.. & update() used from UpdateModelMixin
    def put(self , request , pk):
        return self.update(request , pk)
        
    # it handles HTTP DELETE request from GenericAPIView.. & destroy() used from DestroyModelMixin
    def delete(self , request , pk):
        return self.destroy(request , pk)
        
'''

# using generics we can easily handle HTTP request.
# the following ListAPIView , CreateAPIView helps us to handle list & create courses

# class CourseLists(generics.ListAPIView , generics.CreateAPIView):
#     queryset = Courses.objects.all()
#     serializer_class = CourseSerialzer


# the following RetrieveAPIView , UpdateAPIView and DestroyAPIView help us to handle get , update & delete courses by ID.

# class CourseModification(generics.RetrieveAPIView , generics.UpdateAPIView , generics.DestroyAPIView):
#     queryset = Courses.objects.all()
#     serializer_class = CourseSerialzer


# using ViewSet we can easily handle HTTP Request in a single class

# class CourseViewSet(ViewSet):
#     def list(self, request):
#         course = Courses.objects.all()
#         serializer = CourseSerialzer(course, many=True)
#         return Response(serializer.data, status=200)


#     def create(self , request):
#         serializer = CourseSerialzer(data = request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data )
#         return Response(serializer.errors )

#     def retrieve(sef, request, pk):
#         try:
#             course = Courses.objects.get(pk=pk)
#         except Courses.DoesNotExist:
#             return Response({"message": "Course ID does not exist "}, status=401)
#         serializer = CourseSerialzer(course)
#         return Response(serializer.data, status=200)


# the ModelViewSet automatically perform add , edit , delete & get courses , we dosen't
# need to any method to execute CRUD opreation.
class CourseViewSet(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CourseSerialzer


## Nested Serializer Example between Instructor and Subjects model 

from rest_framework.permissions import IsAuthenticated 

class InstructorList(generics.ListCreateAPIView):
  
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

# to check authetication..id user is loged in or not
class SubjectsList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer