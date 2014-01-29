from django.db import models

# Create your models here.
class musteri(models.Model):

    
    isim = models.CharField(max_length=120)
    sirket = models.CharField(max_length=120)
    adres = models.TextField(max_length=250)
    siparis =models.TextField(max_length=250)
    email =models.EmailField()
    web =models.URLField()
    class Meta:
        verbose_name_plural ='Musteri'

    def __unicode__(self):
        return self.isim
    

class aktivite(models.Model):
    durum = models.CharField(max_length=60)
    gorev = models.TextField(max_length=250)
    kurum = models.CharField(max_length=120, verbose_name ='Kurum/Kisi')
    tarih = models.DateTimeField('Son Tarih')
    gorevli = models.CharField(max_length=120)
    sonuc = models.TextField(max_length =250)
    class Meta:
        verbose_name_plural='Aktivite'
        
    def __unicode__(self):
        return self.gorev
    
