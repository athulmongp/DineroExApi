from django.shortcuts import render
from .models import *
from rest_framework import generics,permissions
from rest_framework .views import APIView
from rest_framework.response import Response
from .serializer import *
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from rest_framework import status
from django.contrib.auth.models import User
from  datetime import date
from django.http import HttpRequest, HttpResponse
from rest_framework.exceptions import ValidationError


def  Homepage(request):
    
    return render(request,'home.html')

class deatils(generics.ListAPIView): 
    queryset = User.objects.all() 
    serializer_class = Person_Details

class deatils2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personn.objects.all()
    serializer_class = Person_Details
class CustomLoginView(KnoxLoginView):
    serializer_class = CustomLoginSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data.get('user', None)

        if user is not None and user.is_active:
            _, token = AuthToken.objects.create(user)
            return Response({'auth_token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED) 
        


         

# ----moduleList-----
        
class ModuleListCreationview(generics.CreateAPIView):
    queryset = ModuleList.objects.all() 
    serializer_class = ModuleListSerializer(queryset, many=True)
    
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = ModuleListSerializer(data=request.data)
        if  ModuleList.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This is Already Exists')
        if serializer.is_valid():
            serializer.validated_data['createdBy'] = self.request.user.username
            serializer.validated_data['createdDate'] = date.today()
            serializer.validated_data['lastMoodifiedBy'] = self.request.user.username
            serializer.validated_data['lastMoodifiedDate'] = date.today()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class ModuleListGetview(generics.ListAPIView):
    queryset = ModuleList.objects.all()
    serializer_class = ModuleListSerializer
    permission_classes = [permissions.IsAuthenticated]
   
    def get(self, request, *args, **kwargs):
        modulename = self.request.query_params.get('name')
        moduleid = self.request.query_params.get('id')

        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            queryset = ModuleList.objects.all()
            if modulename:
                if len(modulename) < 3:
                    raise ValidationError("Name must be at least 3 characters long.")
                queryset = queryset.filter(name__icontains=modulename[:3])  
            if moduleid:
                queryset = queryset.filter(id=moduleid)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)


class ModuleListEditView(generics.UpdateAPIView):
    queryset = ModuleList.objects.all()
    serializer_class = ModuleListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk, format=None):
        
        instance = self.get_object()
         
        serializer = self.get_serializer(instance, data=request.data)
          
        if  ModuleList.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This is Already Exists')
        if serializer.is_valid():
            serializer.validated_data['lastMoodifiedBy'] = self.request.user.username
            serializer.validated_data['lastMoodifiedDate'] = date.today()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ModuleListDeleteView(generics.DestroyAPIView):
    queryset = ModuleList.objects.all()
    serializer_class = ModuleListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, format=None):
        instance = self.get_object()
        
        instance.delete()
        message = 'ModuleList with id {} has been deleted'.format(pk)
        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)
    


# ----moduleListPermission-----
    
class ModuleListPermissionCreationview(generics.CreateAPIView):
    queryset = ModulePermission.objects.all() 
    serializer_class = ModulePermissionSerializer(queryset, many=True)
    
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = ModulePermissionSerializer(data=request.data)
        if  ModulePermission.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This is Already Exists')
        if serializer.is_valid():
            serializer.validated_data['createdBy'] = self.request.user.username
            serializer.validated_data['createdDate'] = date.today()
            serializer.validated_data['lastMoodifiedBy'] = self.request.user.username
            serializer.validated_data['lastMoodifiedDate'] = date.today()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class ModuleListPermissionGetview(generics.ListAPIView):
    queryset = ModulePermission.objects.all() 
    serializer_class = ModulePermissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        userid = self.request.query_params.get('userid')
        moduleid = self.request.query_params.get('moduleid')
    
        
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            queryset = ModulePermission.objects.all()
            if userid :
                queryset = queryset.filter(userid=userid)  
            if moduleid:
                queryset = queryset.filter(moduleid=moduleid)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)


class ModuleListPermissionEditView(generics.UpdateAPIView):
    queryset = ModulePermission.objects.all() 
    serializer_class = ModulePermissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, pk, format=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
         
        if  ModulePermission.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This is Already Exists')
        if serializer.is_valid():
            serializer.validated_data['lastMoodifiedBy'] = self.request.user.username
            serializer.validated_data['lastMoodifiedDate'] = date.today()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    

class ModuleListPermissionDeleteView(generics.DestroyAPIView):
    queryset = ModulePermission.objects.all()
    serializer_class = ModulePermissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, format=None):
        instance = self.get_object()
        
        instance.delete()
        message = 'ModuleListPermission with id {} has been deleted'.format(pk)
        return Response({'message': message}, status=status.HTTP_204_NO_CONTENT)

    


# class ModuleListGetview(generics.ListAPIView):
#     queryset = ModuleList.objects.all() 
#     serializer_class = ModuleListSerializer
#     permission_classes = [permissions.IsAuthenticated]  
    
# class ModuleListEditview(generics.UpdateAPIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def put(self, request, pk, format=None):
#         queryset  = self.get_object(pk)
#         serializer = ModuleListSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     





    # def post(self, request, format=None):
    #     if  ModuleList.objects.filter(**request.data).exists():
    #         raise serializers.ValidationError('This is Already Exists')
        

        
    #     self.createdBy=self.request.user.username,
    #     self.createdDate = date.today(), 
    #     self.lastMoodifiedBy = self.request.user.username,
    #     self.lastMoodifiedDate=date.today()
    #     self.save()     

# class ModuleListDetailsview(generics.ListCreateAPIView): 

#     queryset = ModuleList.objects.all() 
#     serializer_class = ModuleListSerializer   
        


# class ModuleListUpdationView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ModuleListSerializer
#     queryset = ModuleList.objects.all()
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_update(self, serializer):
#         instance = self.get_object()  
#         common_instance = instance.commonId
#         datas = ModuleList.objects.get(id=common_instance)
#         common_instance = CommonFields.objects.get(id=datas.commonId)
        

#         common_instance.lastModifiedBy = self.request.user.username
#         common_instance.lastModifiedDate = date.today()
#         common_instance.save()

#         serializer.save()        




# class ModuleListUpdationView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ModuleListSerializer
#     queryset = ModuleList.objects.all() 
#     print(queryset)
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         instance_id = serializer.id
#         print(instance_id)
#         datas = ModuleList.objects.get(id=instance_id)
     
#         common_instance  = CommonFields.objects.get(id = datas.commonId )
        
#         common_instance.lastMoodifiedBy = self.request.user.username
#         common_instance.lastMoodifiedDate=date.today()
#         common_instance.save()
        # serializer.save(commonId=common_instance)   



# class moduleListView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ModuleListSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data.get('user', None)

#         if user is not None and user.is_active:
#             common = CommonFields(createdBy=request.user.username)
           
#             return Response({'detail': 'Module created successfully'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
 
    

               

 
