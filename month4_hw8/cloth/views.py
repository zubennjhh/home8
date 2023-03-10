from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms


class ProductTagFirstView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Юбки")
    template_name = "product_tag_one.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Юбки")


class ProductTagSecondView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Штаны")
    template_name = "product_tag_second.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Штаны")


class ProductTagThirdView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Верхняя одежда")
    template_name = "product_tag_third.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Верхняя одежда")


class ProductFourthView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name="Футболки")
    template_name = "product_tag_fourth.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name="Футболки")


class ProductListView(ListView):
    queryset = models.ProductCL.objects.filter().order_by('-id')
    template_name = "product_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter().order_by('-id')


class OrderCreateView(CreateView):
    template_name = "add_order.html"
    form_class = forms.OrderCLForm
    success_url = "/cloth/"
    queryset = models.OrderCL.objects.all()

    def form_valid(self, form):
        return super(OrderCreateView, self).form_valid(form=form)
