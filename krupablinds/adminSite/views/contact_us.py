

from adminSite.views.file_import import * 


##############################  contact us  ##############################


def show_contact(request):
    contact_obj = ContactUs.objects.all()
    context={
        'contact_obj':contact_obj,
    }
    return render(request,'adminAppTemplates/contact_us/list_contact.html',context)
    

def add_contact(request):
    if(request.method=="POST"):
        if(request.POST['contact_id']==''):
            print("inside add ")
            person_name=request.POST['person_name']
            email=request.POST['email']
            comment=request.POST['comment']
            ###########################
            contact_obj = ContactUs()
            contact_obj.person_name = person_name
            contact_obj.email = email
            contact_obj.comment = comment
            contact_obj.save()
            
            

            return redirect('show_contact')
        else:
            print("inside update")

            person_name=request.POST['person_name']
            email=request.POST['email']
            comment=request.POST['comment']

            contact_obj=ContactUs.objects.get(id=request.POST['contact_id'])

            ###########################
            
            contact_obj.person_name = person_name
            contact_obj.email = email
            contact_obj.comment = comment
            contact_obj.save()
            return redirect('show_contact')
            

    else:
        context={
            "data":"Add Contact Us",
        }

        return render(request,'adminAppTemplates/contact_us/add_contact.html',context)



def update_contact(request,id):
    contact_obj=ContactUs.objects.get(id=id)

    context={
        "contact_obj":contact_obj,
        "data":"Update Contact Us",
    }
    return render(request,'adminAppTemplates/contact_us/add_contact.html',context)



def delete_contact(request, id):
    contact_obj = ContactUs.objects.get(id=id)
    contact_obj.delete()
        
    return redirect('show_contact')

