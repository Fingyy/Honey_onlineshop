from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from shop.forms import HoneyForm
from shop.models import Honey


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


class HoneyCreateView(CreateView):
    template_name = 'honey/honey_create.html'
    model = Honey
    form_class = HoneyForm
    success_url = reverse_lazy('honey_list')


class HoneyUpdateView(UpdateView):
    template_name = 'honey/honey_create.html'
    model = Honey
    form_class = HoneyForm
    success_url = reverse_lazy('honey_list')


class HoneyDeleteView(DeleteView):
    template_name = 'honey/honey_delete.html'
    model = Honey
    success_url = reverse_lazy('honey_list')
