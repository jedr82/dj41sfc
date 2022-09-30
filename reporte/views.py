from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa

from cmp.models import Proveedor, ComprasEnc


# Create your views here.
class ReporteCompras(TemplateView):
    template_name = 'reporte/reporte_compras.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de las Compras'
        return context

class FacturaPDFView(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('reporte/factura_compra.html')
            context = {
                'comp': {
                    'name': 'AR ELECTRICIDAD S.R.L.',
                    'ruc': '80009317-8',
                    'address': 'Av. Fernando de la Mora 3424 c/ Av. Cacique Lambaré'
                },
                'compracab': ComprasEnc.objects.get(pk=self.kwargs['pk'])
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            pisaStatus = pisa.CreatePDF(
                html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('cmp_app:compras_list'))