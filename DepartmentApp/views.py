from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.


def home(request):
    return render(request, 'index_department.html')


class OrganizationCreateView(CreateView):
    """
        Creted organization data.
    """
    
    form_class = OrganizationForm
    template_name = 'Organization_create.html'

    def form_valid(self, form):
      data = form.save(commit=False)
      data.save()
      return redirect('departmentapp:organizationcreate')


class OrganizationListView(ListView):
    """
        Display the all organisation data in listview.
    """
    template_name = 'Organization_list.html'
    model = Organization


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DepartmentCreateView(CreateView):
    """
        Creted Department data.
    """
    form_class = DepartmentForm
    template_name = 'Department_create.html'
    
    def form_valid(self, form):
      data = form.save(commit=False)
      data.save()
      return redirect('departmentapp:departmentlist')


class DepartmentListView(ListView):
    """
        Display the all  data in listview.
    """
    # template_name = 'Department_list.html'
    template_name = 'Department/department.html'

    model = Department

    # context_object_name = "department"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DepartmentUpdateView(UpdateView):
    """
        This class is used for updating of a particular Department.
    """
    model = Department
    form_class = DepartmentForm
    template_name = 'Department_update.html'

    success_url = '/department/department_list/'

    def get_form_kwargs(self):
        kwargs = super(DepartmentUpdateView, self).get_form_kwargs()
        kwargs.update()
        return kwargs

class DepartmentDetailView(DetailView):
    """
        User can see detail of the department.
    """
    model = Department
    template_name = 'Department_deatil.html'

     # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(DepartmentDetailView,
             self).get_context_data(*args, **kwargs)

        context['department'] = Department.objects.get(dept_id = self.kwargs['pk'])
        return context

class DepartmentDeleteView(DeleteView):
    """
        User can delete of the department.
    """
    template_name = 'Department_delete.html'
    model = Department
    success_url = '/department/department_list/'




