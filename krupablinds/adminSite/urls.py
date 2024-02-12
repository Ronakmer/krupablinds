# from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

######### file import #########
from adminSite.views.file_import import * 
from adminSite.views.role_permission import * 
from adminSite.views.contact_us import * 
from adminSite.views.awning_type import * 
from adminSite.views.fabric_type import * 









urlpatterns = [


    path('', dashboard, name="dashboard"),        
    path('login_page/', login_page, name="login_page"),        




    # user-role
    path('add-role/', add_role,  name="add_role"),
    path('show-role/',show_role, name="show_role"),
    path('delete-role/<int:id>', delete_role, name="delete_role"),
    path('update-role/<int:id>',update_role, name="update_role"),

    # user-role
    path('add-permission/', add_permission,  name="add_permission"),
    path('show-permission/',show_permission, name="show_permission"),
    path('delete-permission/<int:id>', delete_permission, name="delete_permission"),
    path('update-permission/<int:id>',update_permission, name="update_permission"),

    # contact us
    path('add-contact/', add_contact,  name="add_contact"),
    path('show-contact/',show_contact, name="show_contact"),
    path('delete-contact/<int:id>', delete_contact, name="delete_contact"),
    path('update-contact/<int:id>',update_contact, name="update_contact"),

    # fabric type
    path('add-fabric/', add_fabric,  name="add_fabric"),
    path('show-fabric/',show_fabric, name="show_fabric"),
    path('delete-fabric/<int:id>', delete_fabric, name="delete_fabric"),
    path('update-fabric/<int:id>',update_fabric, name="update_fabric"),

    # awning type
    path('add-awning/', add_awning,  name="add_awning"),
    path('show-awning/',show_awning, name="show_awning"),
    path('delete-awning/<int:id>', delete_awning, name="delete_awning"),
    path('update-awning/<int:id>',update_awning, name="update_awning"),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

