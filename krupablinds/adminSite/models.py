from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  

# Create your models here.

# Length :- min 10
# Width:- min 5 max 10
# Length kar ta width  -2 hovi jaoy



##############################  user role  ##############################

class user_role(models.Model):
    user_roles=models.CharField(max_length=55, default="",null=True,blank=True)
    # status=models.CharField(max_length=25, default="True")
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(auto_now=True)


##############################  permission  ##############################

class permission(models.Model):
    permission_name=models.CharField(max_length=55,default="",null=True,blank=True)
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(auto_now=True)


##############################  role_has_permissions  ##############################

class role_has_permissions(models.Model):
    permission_id=models.ForeignKey(to=permission,on_delete=models.CASCADE)
    role_id=models.ForeignKey(to=user_role,on_delete=models.CASCADE)


##############################  contact us  ##############################

class ContactUs(models.Model):
    person_name=models.CharField(max_length=55, default="",null=True,blank=True)
    email = models.EmailField(max_length = 55,null=True,blank=True)
    comment=models.TextField(null=True,blank=True)
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(auto_now=True)




##############################  Fabric Type  ##############################

class FabricType(models.Model):

    fabric_name=models.CharField(max_length=55, default="",null=True,blank=True)
    fabric_color=models.CharField(max_length=55, default="",null=True,blank=True)
    fabric_price=models.FloatField(null=True,blank=True)
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(auto_now=True)


##############################  Awning Type  ##############################

class AwningType(models.Model):

    awning_name=models.CharField(max_length=55, default="",null=True,blank=True)
    awning_color=models.CharField(max_length=55, default="",null=True,blank=True)
    awning_price=models.FloatField(null=True,blank=True)
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(auto_now=True)


##############################  Attachment  ##############################

class Attachment(models.Model):

    attachment_name=models.CharField(max_length=55, default="",null=True,blank=True)
    attachment_price=models.FloatField(null=True,blank=True)
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(auto_now=True)



##############################  Cost  ##############################

class Cost(models.Model):
    fabrictype_id=models.ForeignKey(to=FabricType,on_delete=models.CASCADE)
    awningtype_id=models.ForeignKey(to=AwningType,on_delete=models.CASCADE)
    total=models.FloatField(null=True,blank=True)
    createDate=models.DateTimeField(default=timezone.now)
    updateDate=models.DateTimeField(auto_now=True)
