from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Trabajo

# Create your views here.
class IndexView(TemplateView):
    template_name = 'trabajos/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cds'] = Trabajo.objects.all().filter(cdRDC=True).count()
        return context
