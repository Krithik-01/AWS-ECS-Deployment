from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate,TaskUpdate,TaskDelete,TaskLogin,TaskRegister
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("",TaskList.as_view(),name='tasklist'),
    path("taskcreate/",TaskCreate.as_view(),name='taskcreate'),
    path("task/<int:pk>",TaskDetail.as_view(),name='taskdetail'),
    path("taskupdate/<int:pk>",TaskUpdate.as_view(),name='taskupdate'),
    path("taskdelete/<int:pk>",TaskDelete.as_view(),name='taskdelete'),
    path("tasklogin/",TaskLogin.as_view(),name='tasklogin'),
    path("taskregister/",TaskRegister.as_view(),name='taskregister'),    
    path("tasklogout/",LogoutView.as_view(next_page='tasklogin'),name='tasklogout')

]