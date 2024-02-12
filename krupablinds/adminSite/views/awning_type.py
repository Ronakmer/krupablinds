

from adminSite.views.file_import import * 


##############################  AwningType  ##############################


def show_awning(request):
    awning_obj = AwningType.objects.all()
    context={
        'awning_obj':awning_obj,
    }
    return render(request,'adminAppTemplates/awning_type/list_awning.html',context)
    

def add_awning(request):
    if(request.method=="POST"):
        if(request.POST['awning_id']==''):
            print("inside add ")
            awning_name=request.POST['awning_name']
            awning_color=request.POST['awning_color']
            awning_price=request.POST['awning_price']
            ###########################
            awning_obj = AwningType()
            awning_obj.awning_name = awning_name
            awning_obj.awning_color = awning_color
            awning_obj.awning_price = awning_price
            awning_obj.save()
            
            

            return redirect('show_awning')
        else:
            print("inside update")

            awning_name=request.POST['awning_name']
            awning_color=request.POST['awning_color']
            awning_price=request.POST['awning_price']

            awning_obj=AwningType.objects.get(id=request.POST['awning_id'])

            ###########################
            
            awning_obj.awning_name = awning_name
            awning_obj.awning_color = awning_color
            awning_obj.awning_price = awning_price
            awning_obj.save()
            return redirect('show_awning')
            

    else:
        context={
            "data":"Add awning",
        }

        return render(request,'adminAppTemplates/awning_type/add_awning.html',context)



def update_awning(request,id):
    awning_obj=AwningType.objects.get(id=id)

    context={
        "awning_obj":awning_obj,
        "data":"Update Awning",
    }
    return render(request,'adminAppTemplates/awning_type/add_awning.html',context)



def delete_awning(request, id):
    awning_obj = AwningType.objects.get(id=id)
    awning_obj.delete()
        
    return redirect('show_awning')



