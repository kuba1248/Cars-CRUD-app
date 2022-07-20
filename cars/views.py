from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from cars.models import Brand, Cars
from cars.forms import CarsForm, BrandForm


# Create your views here.


class MainView(LoginRequiredMixin, ListView):
    paginate_by = 7
    model = Cars

    def listing(self, request, page):
        brand_list = Brand.objects.all().count()
        users = Cars.objects.all().order_by("-id")
        paginator = Paginator(users, per_page=7)  # 5 users per page
        page_object = paginator.get_page(page)
        context = {'ml': brand_list, "page_obj": page_object}

        return render(request, 'cars/cars_list.html', context)

    # def get(self, request):
    #     brand_list = Brand.objects.all().count()
    #     car_list = Cars.objects.all()
    #
    #     context = {'ml': brand_list, 'cl': car_list}
    #     return render(request, 'cars/car_list.html', context)


def listing(request, page):
    brand_list = Brand.objects.all().count()
    users = Cars.objects.all().order_by("id")
    paginator = Paginator(users, per_page=7)  # 5 users per page
    page_object = paginator.get_page(page)

    context = {'ml': brand_list, "page_obj": page_object}

    return render(request, 'cars/cars_list.html', context)


class carListView(View):

    def get(self, request, id):
        brand_list = Brand.objects.all().count()
        car_list = Cars.objects.filter(id=id)
        # .objects.filter(id=id)
        context = {'ml': brand_list, 'cl': car_list}

        return render(request, 'cars/car_detail.html', context)


class brandDetailView(View):
    model = Brand

    # def listing(self, request, page):
    #     brand_list = Cars.objects.all().count()
    #     users = Cars.objects.all().filter("-brand")
    #     paginator = Paginator(users, per_page=7)  # 5 users per page
    #     page_object = paginator.get_page(page)
    #     context = {'ml': brand_list, "page_obj": page_object}
    #
    #     return render(request, 'cars/brand_detail.html', context)

    def get(self, request, id):
        brand_list = Brand.objects.all().count()
        brand_spisok = Brand.objects.filter(id=id)

        # if Brand.Brand == Cars.brand:
        car_list = Cars.objects.all()
        # .objects.filter(id=id)
        context = {'ml': brand_list, 'cl': brand_spisok, 'clist': car_list}

        return render(request, 'cars/brand_detail.html', context)


class brandListView(ListView):
    model = Brand
    context_object_name = 'brand_list'
    template_name = 'cars/brand_list.html'
    success_url = reverse_lazy('index')


#     paginate_by = 7
#     model = Brand
#
#     def listing2(self, request, page):
#         car_list = Cars.objects.all().count()
#         users = Brand.objects.all().order_by("-id")
#         paginator = Paginator(users, per_page=7)  # 5 users per page
#         page_object = paginator.get_page(page)
#         context = {'ml': car_list, "page_obj": page_object}
#
#         return render(request, 'cars/brand_list.html', context)
#
#     # def get(self, request):
#     #     brand_list = Brand.objects.all().count()
#     #     car_list = Cars.objects.all()
#     #
#     #     context = {'ml': brand_list, 'cl': car_list}
#     #     return render(request, 'cars/car_list.html', context)
#
#
# def listing2(request, page):
#     car_list = Cars.objects.all().count()
#     users = Brand.objects.all().order_by("id")
#     paginator = Paginator(users, per_page=7)  # 5 users per page
#     page_object = paginator.get_page(page)
#
#     context = {'ml': car_list, "page_obj": page_object}
#
#     return render(request, 'cars/brand_list.html', context)


class brandSpisokView(ListView):
    model = Brand
    context_object_name = 'brand_spisok'
    template_name = 'cars/brand_spisok.html'
    success_url = reverse_lazy('index')

    paginate_by = 7

    def listing2(self, request, page):
        car_list = Cars.objects.all().count()
        users = Brand.objects.all().order_by("-id")
        paginator = Paginator(users, per_page=7)  # 5 users per page
        page_object = paginator.get_page(page)
        context = {'ml': car_list, "page_obj": page_object}

        return render(request, 'cars/brand_spisok.html', context)

    # def get(self, request):
    #     brand_list = Brand.objects.all().count()
    #     car_list = Cars.objects.all()
    #
    #     context = {'ml': brand_list, 'cl': car_list}
    #     return render(request, 'cars/car_list.html', context)


def listing2(request, page):
    car_list = Cars.objects.all().count()
    users = Brand.objects.all().order_by("id")
    paginator = Paginator(users, per_page=7)  # 5 users per page
    page_object = paginator.get_page(page)

    context = {'ml': car_list, "page_obj": page_object}

    return render(request, 'cars/brand_spisok.html', context)


class brandCreateView(CreateView):
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('brand_spisok')


class brandUpdateView(UpdateView):
    model = Brand
    fields = "__all__"
    success_url = reverse_lazy('brand_spisok')


class brandDeleteView(DeleteView):
    model = Brand
    success_url = reverse_lazy('brand_spisok')


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
