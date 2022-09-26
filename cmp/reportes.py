import os
from datetime import timezone

from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

from .models import ComprasEnc,ComprasDet


def link_callback(uri, rel):
    """ Convierte HTML URIs al path absoluto del sistema"""
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list,tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL
        sRoot = settings.STATIC_ROOT
        mUrl = settings.MEDIA_URL
        mRoot = settings.MEDIA_ROOT

        #Convierte los URIs al path absoluto
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    if not os.path.isfile(path):
        raise Exception('media URI must start width %s or %s' % (sUrl, mUrl))

    return path

def reporte_compras(request):
    template_path = 'cmp/compras_print_all.html'
    today = timezone.now()

    compras = ComprasEnc.objects.all()
    context = {
        'obj': compras,
        'today': today,
        'request': request
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="todas_compras.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    #Para crear el pdf
    pisaStatus = pisa.CreatePDF(
        html, det=response, link_callback=link_callback
    )

    if pisaStatus.err:
        return HttpResponse('Tuvimos algunos errores <pre>' + html + '</pre>')
    return response