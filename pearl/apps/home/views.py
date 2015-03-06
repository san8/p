from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/home.html'


class FAQView(TemplateView):
    template_name = 'home/faq.html'


class ErrorView(TemplateView):
    template_name = 'home/500.html'
