from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from shop.forms import HoneyForm,HoneyProductOnStockForm, PackagingForm
from shop.models import Honey, HoneyProductOnStock, Packaging


class BaseView(TemplateView):
    template_name = 'home.html'


class AboutUsView(TemplateView):
    template_name = 'about_us.html'


class HoneyListView(ListView):
    template_name = 'honey/honey_list.html'
    model = Honey
    context_object_name = 'honey_list'

    def get_queryset(self):
        gueryset = Honey.objects.all()
        return gueryset


class HoneyDetailView(DetailView):
    template_name = 'honey/honey_detail.html'
    model = Honey
    context_object_name = 'honey'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        honey = self.get_object()
        context["is_med_akatovy"] = honey.pk == 1
        context["is_med_kvetovy"] = honey.pk == 2
        return context


class HoneyCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'honey/honey_create.html'
    model = Honey
    form_class = HoneyForm
    success_url = reverse_lazy('honey_list')

    def test_func(self):
        return self.request.user.is_superuser


class HoneyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'honey/honey_create.html'
    model = Honey
    form_class = HoneyForm

    def test_func(self):
        if not self.request.user.is_superuser:
            raise PermissionDenied
        return True

    '''
    Jelikož do UpdateView mohu vstupovat z více šablon, tak pomocí next zajistím, že se vždy vrátím na předchozí 
    stránku a ne vždy do přdem definované success_url
    '''
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('honey_list')


class HoneyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'honey/honey_delete.html'
    model = Honey

    def test_func(self):
        return self.request.user.is_superuser

    '''
    Jelikož do DeleteView mohu vstupovat z více šablon, tak pomocí next zajistím, že se vždy vrátím na předchozí 
    stránku a ne vždy do přdem definované success_url
    '''
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('honey_list')


class PackagingCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'packaging/packaging_create.html'
    model = Packaging
    form_class = PackagingForm

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('stock_prod_list')


class PackingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'packaging/packaging_create.html'
    model = Packaging
    form_class = PackagingForm
    success_url = reverse_lazy('honey_list')

    def test_func(self):
        return self.request.user.is_superuser


class PackagingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'packaging/packaging_delete.html'
    model = Packaging
    form_class = PackagingForm
    success_url = reverse_lazy('honey_list')

    def test_func(self):
        return self.request.user.is_superuser


class HoneyProductOnStockCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'product_in_stock/prod_in_stock_create.html'
    model = HoneyProductOnStock
    form_class = HoneyProductOnStockForm

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('stock_prod_list')


class HoneyProductOnStockListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'product_in_stock/prod_in_stock_list.html'
    model = HoneyProductOnStock
    context_object_name = 'items_on_stock'

    def test_func(self):
        return self.request.user.is_superuser


class HoneyProductOnStockUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'product_in_stock/prod_in_stock_create.html'
    model = HoneyProductOnStock
    form_class = HoneyProductOnStockForm

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('stock_prod_list')


class HoneyProductOnStockDeleteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'product_in_stock/prod_in_stock_delete.html'
    model = HoneyProductOnStock
    form_class = HoneyProductOnStockForm

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('stock_prod_list')
