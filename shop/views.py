from django.views.generic import TemplateView


class BaseView(TemplateView):
    template_name = 'home.html'


class AboutUsView(TemplateView):
    template_name = 'about_us.html'
