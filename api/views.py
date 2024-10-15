from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status, serializers
# Create your views here.


@api_view(['GET'])
def api_overview(request):
    api_urls= {
        'All Items': '/',
        'Add Students': 'api/add-students/',
        'View Students': 'api/view-students/',
        'Search by Parameters': 'api/view-students/?parameter_name=parameter',
        "For Example": "api/view-students/?roll_number=20368",
        'Update Student': 'api/update-student/roll_number/',
        'Delete Student': 'api/delete-student/roll_number',
    }

    return Response(api_urls)

# Create API

@api_view(['POST'])
def add_students(request):

    student= StudentSerializer(data=request.data)

    if Student.objects.filter(roll_number=request.data.get('roll_number')).exists():
        raise serializers.ValidationError(f"The roll number {request.data.get('roll_number')} is already exists")
    
    if student.is_valid():
        student.save()
        return Response(student.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Read API

@api_view(['GET'])
def view_students(request):
    if request.query_params:
        students= Student.objects.filter(**request.query_params.dict())
    else:
        students= Student.objects.all()
    if students:
        serializer= StudentSerializer(students, many= True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# Update API 

@api_view(['GET', 'POST'])
def update_student(request, pk):
    try:
        student= Student.objects.get(roll_number=pk)
    except Student.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
    serializer= StudentSerializer(instance=student, data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Delete API 

@api_view(['GET', 'DELETE'])
def delete_student(request, pk):
    try:
        student= Student.objects.get(roll_number=pk)
        serializer= StudentSerializer(student)
        student.delete()
        return Response({"message": f"{student.name} is removed from the Students Database", "data": serializer.data}, status=status.HTTP_200_OK)
    
    except Student.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)