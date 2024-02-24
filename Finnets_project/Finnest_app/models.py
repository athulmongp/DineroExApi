from django.db import models
from django.contrib.auth.models import User

class Personn(models.Model):  
    Name = models.CharField(max_length = 30)


             

class ModuleList(models.Model):
    name = models.CharField(max_length = 50,null = True,blank = True)
    createdBy = models.CharField(max_length = 50,null = True,blank = True)
    createdDate = models.DateField(null = True,blank = True) 
    lastMoodifiedBy = models.CharField(max_length = 50,null = True,blank = True)
    lastMoodifiedDate = models.DateField(null = True,blank = True)  


class ModulePermission(models.Model):
    moduleid = models.ForeignKey(ModuleList,null = True,on_delete = models.CASCADE)   
    userid = models.ForeignKey(User,null = True,on_delete = models.CASCADE)  
    
    # moodule tabile permission
    canAccess = models.BooleanField(default = False)
    canCreate = models.BooleanField(default = False)
    canEdit = models.BooleanField(default = False)
    canDelete = models.BooleanField(default = False)

    createdBy = models.CharField(max_length = 50,null = True,blank = True)
    createdDate = models.DateField(null = True,blank = True)
    lastMoodifiedBy = models.CharField(max_length = 50,null = True,blank = True)
    lastMoodifiedDate = models.DateField(null = True,blank = True) 


