from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from base.models import Enquiry


# Create your views here.
class EnquiryList(ListView):
    model = Enquiry
    context_object_name = 'enquiries'


class EnquiryCreate(CreateView):
    model = Enquiry
    fields = '__all__'
    success_url = reverse_lazy('enquiry')


class EnquiryDelete(DeleteView):
    model = Enquiry
    context_object_name = 'enquiry'
    success_url = reverse_lazy('enquiry')


class EnquiryDetail(DetailView):
    model = Enquiry
    context_object_name = 'enquiry'


class EnquiryUpdate(UpdateView):
    model = Enquiry
    fields = '__all__'
    success_url = reverse_lazy('enquiry')
