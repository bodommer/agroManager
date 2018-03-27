from django.forms import ModelForm

from spravaPoli.model.Cast import Cast
from spravaPoli.model.Plodina import Plodina
from spravaPoli.model.Vysadba import Vysadba
from spravaPoli.model.Zber import Zber


class NovaCastForm(ModelForm):
    class Meta:
        model = Cast
        fields = ['meno', 'rozloha']

class NovaPlodinaForm(ModelForm):
    class Meta:
        model = Plodina
        fields = ['meno']

class NovaVysadbaForm(ModelForm):
    class Meta:
        model = Vysadba
        fields = ['datumVysadby', 'casVysadby', 'naklady', 'vysadeneMnozstvo']

class NovyZberForm(ModelForm):
    class Meta:
        model = Zber
        fields = ['datumZberu', 'casZberu', 'uroda', 'zisk']