from django.http import HttpResponse
from django.template import Context, loader

from crm.models import aktivite


def anasayfaView(request):
    aktiviteler = aktivite.objects.all()
    sablon = loader.get_template('anasayfa.html')
    icerik = Context({
                      'baslik': 'CRM sistemine hosgeldiniz:)',
                      'aktiviteler': aktiviteler 
                      })
    yanit = sablon.render(icerik)
    return HttpResponse(yanit)
#commit# Create your views here.
