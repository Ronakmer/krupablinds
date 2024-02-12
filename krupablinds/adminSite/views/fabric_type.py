

from adminSite.views.file_import import * 


##############################  FabricType  ##############################


def show_fabric(request):
    fabric_obj = FabricType.objects.all()
    context={
        'fabric_obj':fabric_obj,
    }
    return render(request,'adminAppTemplates/fabric_type/list_fabric.html',context)
    

def add_fabric(request):
    if(request.method=="POST"):
        if(request.POST['fabric_id']==''):
            print("inside add ")
            fabric_name=request.POST['fabric_name']
            fabric_color=request.POST['fabric_color']
            fabric_price=request.POST['fabric_price']
            ###########################
            fabric_obj = FabricType()
            fabric_obj.fabric_name = fabric_name
            fabric_obj.fabric_color = fabric_color
            fabric_obj.fabric_price = fabric_price
            fabric_obj.save()
            
            

            return redirect('show_fabric')
        else:
            print("inside update")

            fabric_name=request.POST['fabric_name']
            fabric_color=request.POST['fabric_color']
            fabric_price=request.POST['fabric_price']

            fabric_obj=FabricType.objects.get(id=request.POST['fabric_id'])

            ###########################
            
            fabric_obj.fabric_name = fabric_name
            fabric_obj.fabric_color = fabric_color
            fabric_obj.fabric_price = fabric_price
            fabric_obj.save()
            return redirect('show_fabric')
            

    else:
        context={
            "data":"Add Fabric",
        }

        return render(request,'adminAppTemplates/fabric_type/add_fabric.html',context)



def update_fabric(request,id):
    fabric_obj=FabricType.objects.get(id=id)

    context={
        "fabric_obj":fabric_obj,
        "data":"Update Fabric",
    }
    return render(request,'adminAppTemplates/fabric_type/add_fabric.html',context)



def delete_fabric(request, id):
    fabric_obj = FabricType.objects.get(id=id)
    fabric_obj.delete()
        
    return redirect('show_fabric')

