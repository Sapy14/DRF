from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Equipment,Executive
from .serializers import EquipmentSerializers,ExecutiveSerializers
from rest_framework import status

#Equipment class based views
class AppList(APIView):
    
    def get(self,request):
        equipment=Equipment.objects.all()
        serializer= EquipmentSerializers(equipment,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=EquipmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class APPListDetails(APIView):
    
    def get(self,request,pk):
        try:
            equipment=Equipment.objects.get(pk=pk)
        except Equipment.DoesNotExist:
            return Response({'Error':'Equipment does not exist'},status=status.HTTP_404_NOT_FOUND)
        serializer=EquipmentSerializers(equipment)
        return Response(serializer.data)
    
    def put(self,request,pk):
        equipment=Equipment.objects.get(pk=pk)
        serializer=EquipmentSerializers(equipment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        equipment=Equipment.objects.get(pk=pk)
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#User class based views

class UserList(APIView):
    
    def get(self,request):
        executive=Executive.objects.all()
        serializer= ExecutiveSerializers(executive,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=ExecutiveSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class UserListDetails(APIView):
    
    def get(self,request,pk):
        try:
            executive=Executive.objects.get(pk=pk)
        except Executive.DoesNotExist:
            return Response({'Error':'Executive does not exist'},status=status.HTTP_404_NOT_FOUND)
        serializer=ExecutiveSerializers(executive)
        return Response(serializer.data)
    
    def put(self,request,pk):
        executive=Executive.objects.get(pk=pk)
        serializer=ExecutiveSerializers(executive,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        executive=Executive.objects.get(pk=pk)
        executive.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
        
    
    
