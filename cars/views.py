from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.generic import View

from cars.models import Brand, Cars
from cars.forms import CarsForm, BrandForm


# Create your views here.

class MainView(View):
    def get(self, request):
        brand_list = Brand.objects.all().count()
        car_list = Cars.objects.all()

        context = {'ml': brand_list, 'cl': car_list}
        return render(request, 'cars/car_list.html', context)


class carListView(View):
    def get(self, request, id):
        brand_list = Brand.objects.all().count()
        car_list = Cars.objects.filter(id=id)
        # .objects.filter(id=id)
        context = {'ml': brand_list, 'cl': car_list}

        return render(request, 'cars/car_detail.html', context)


class brandListView(ListView):
    model = Brand
    context_object_name = 'brand_list'
    template_name = 'cars/brand_list.html'
    success_url = reverse_lazy('index')


class brandCreateView(CreateView):
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('brand_list')


class brandUpdateView(UpdateView):
    model = Brand
    fields = "__all__"
    success_url = reverse_lazy('brand_list')


class brandDeleteView(DeleteView):
    model = Brand
    success_url = reverse_lazy('brand_list')


class CarsUpdateView(UpdateView):
    model = Cars
    fields = '__all__'
    success_url = reverse_lazy('index')


class CarsCreateView(CreateView):
    model = Cars
    fields = '__all__'
    success_url = reverse_lazy('index')


class CarsDeleteView(DeleteView):
    model = Cars
    success_url = reverse_lazy('index')
