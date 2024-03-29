from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render  ,redirect
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView 
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import  UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from .models import Task
from django.urls import reverse_lazy

# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasklist.html'
    context_object_name='task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = context['task'].filter(user=self.request.user)
        context['count']=context['task'].filter(complete=False).count()
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['task']=context['task'].filter(title__icontains=search_input)
            context[search_input]=search_input
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'taskdetail.html'
    context_object_name='task'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields= ['title','description','complete']
    template_name='task_form.html'
    success_url=reverse_lazy('tasklist')

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model=Task
    fields=['title','description','complete']
    success_url=reverse_lazy('tasklist')
    template_name='task_form.html'

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name='confirm_delete.html'
    success_url=reverse_lazy('tasklist')

class TaskLogin(LoginView):
    template_name='login.html'
    redirect_authenticated_user=False
    fields='__all__'

    def get_success_url(self) -> str:
        return reverse_lazy('tasklist')
    
class TaskRegister(FormView):
    template_name='register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('tasklist')

    def form_valid(self, form):
        user = form.save()  
        if user is not None:
            login(self.request,user)
        return super(TaskRegister,self).form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasklist')
        return super(TaskRegister,self).get(*args,**kwargs)
    
