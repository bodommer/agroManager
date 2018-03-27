from django.contrib import admin
from spravaPoli.model.Pozemok import Pozemok
from spravaPoli.model.Cast import Cast
from spravaPoli.model.Cyklus import Cyklus
from spravaPoli.model.Vysadba import Vysadba
from spravaPoli.model.Zber import Zber
from spravaPoli.model.Plodina import Plodina

admin.site.register(Cast)
admin.site.register(Cyklus)
admin.site.register(Plodina)
admin.site.register(Pozemok)
admin.site.register(Vysadba)
admin.site.register(Zber)

