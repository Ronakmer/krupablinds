

from adminSite.views.file_import import * 


##############################  user role  ##############################


def show_role(request):
    role_obj = user_role.objects.all()
    context={
        'role_obj':role_obj,
    }
    return render(request,'adminAppTemplates/role_permission/list_role.html',context)
    

def add_role(request):
        if(request.method=="POST"):
            if(request.POST['role_id']==''):
                print("inside add ")
                user_roles=request.POST['user_roles']
                ###########################
                user = user_role()
                user.user_roles = user_roles
                user.save()
                
                

                return redirect('show_role')
            else:
                print("inside update")

                user_roles=request.POST['user_roles']

                role_obj=user_role.objects.get(id=request.POST['role_id'])

                ###########################
                
                role_obj.user_roles = user_roles
                role_obj.save()
                return redirect('show_role')
                

        else:
            context={
                "data":"Add Role",
            }

            return render(request,'adminAppTemplates/role_permission/add_role.html',context)



def update_role(request,id):
        role_obj=user_role.objects.get(id=id)

        context={
            "role_obj":role_obj,
            "data":"Update Role",
        }
        return render(request,'adminAppTemplates/role_permission/add_role.html',context)



def delete_role(request, id):
        role_obj = user_role.objects.get(id=id)
        role_obj.delete()
            
        return redirect('show_role')


##############################  permission  ##############################


def show_permission(request):
    permission_obj = permission.objects.all()
    context={
        'permission_obj':permission_obj,
    }
    return render(request,'adminAppTemplates/role_permission/list_permission.html',context)
    


def add_permission(request):
        if(request.method=="POST"):
            if(request.POST['permission_id']==''):
                print("inside add ")
                permission_name=request.POST['permission_name']
                ###########################
                permission_obj = permission()
                permission_obj.permission_name = permission_name
                permission_obj.save()
                
                

                return redirect('show_permission')
            else:
                print("inside update")

                permission_name=request.POST['permission_name']

                permission_obj=permission.objects.get(id=request.POST['permission_id'])

                ###########################
                
                permission_obj.permission_name = permission_name
                permission_obj.save()
                return redirect('show_permission')
                
        else:
            context={
            "data":"Add Permission",
            }

            return render(request,'adminAppTemplates/role_permission/add_permission.html',context)






def update_permission(request,id):
        permission_obj=permission.objects.get(id=id)

        context={
            "permission_obj":permission_obj,
            "data":"Update Permission",
        }
        return render(request,'adminAppTemplates/role_permission/add_permission.html',context)





def delete_permission(request, id):
        permission_obj = permission.objects.get(id=id)
        permission_obj.delete()
            
        return redirect('show_permission')



