from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from app.forms import *
from django.http import HttpResponse
class cbv_form(FormView):
    template_name='cbv_form.html'
    form_class=StudentForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('data is inserted')
