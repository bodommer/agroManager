from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from spravaPoli.models import *
from spravaPoli.forms import *
from spravaPoli.model.Cast import Cast

class GeneralView(generic.View):

    def prehladPola(request):
        casti = Cast.objects.all()
        plodiny = Plodina.objects.all()
        return render(request, 'spravaPoli/prehladPola.html', {'casti': casti, 'plodiny': plodiny})

    def novaCast(request):
        if request.method == 'POST':
            form = NovaCastForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                cast = Cast()
                cast.meno = data['meno']
                cast.rozloha = data['rozloha']
                cast.pozemok = get_object_or_404(Pozemok, pk=1)
                cast.save()
                return HttpResponseRedirect('/sprava/')
        else:
            form = NovaCastForm()
            return render(request, 'spravaPoli/novaCast.html', {'form': form})

    def prehladPlodiny(request, plodina_id):
        cy = Cyklus.objects.filter(plodina_id=plodina_id)
        return render(request, 'spravaPoli/prehladPlodiny.html', {'data': cy})

    def novaPlodina(request):
        if request.method == 'POST':
            form = NovaPlodinaForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                plodina = Plodina()
                plodina.meno = data['meno']
                plodina.save()
                return HttpResponseRedirect('/sprava/')
        else:
            form = NovaPlodinaForm()
            return render(request, 'spravaPoli/novaPlodina.html', {'form': form})

class CastView(generic.View):

    def prehladCasti(request, cast_id):
        if request.method == 'POST':
            cycle = Cyklus()
            cycle.cast_id = cast_id
            pl_id = request.POST.get('plodina_id', '1')
            print(pl_id)
            cycle.plodina_id = int(pl_id)
            cycle.save()
        cy = Cast.objects.filter(id=cast_id)
        plodiny = Plodina.objects.all()
        cykly = Cyklus.objects.filter(cast_id=cast_id)
        return render(request, 'spravaPoli/prehladCasti.html', {'casti': cy, 'cast_id': cast_id, 'cykly':cykly, 'plodiny': plodiny})

    def novaVysadba(request, cast_id, cyklus_id):
        if request.method == 'POST':
            form = NovaVysadbaForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                vys = Vysadba()
                vys.datumVysadby = data['datumVysadby']
                vys.casVysadby = data['casVysadby']
                vys.naklady = data['naklady']
                vys.vysadeneMnozstvo = data['vysadeneMnozstvo']
                vys.cyklus_id = int(request.POST.get('cyklus'))
                vys.save()
                cyklus = Cyklus.objects.get(id=cyklus_id)
                cyklus.vysadba_id = vys.id
                cyklus.save()
                return HttpResponseRedirect('/sprava/cast/' + cast_id)
        else:
            form = NovaVysadbaForm()
        return render(request, 'spravaPoli/novaVysadba.html', {'form': form, 'cast_id': cast_id, 'cyklus_id': cyklus_id})

    def novyZber(request, cast_id, cyklus_id):
        if request.method == 'POST':
            form = NovyZberForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                zber = Zber()
                zber.datumZberu = data['datumZberu']
                zber.casZberu = data['casZberu']
                zber.uroda = data['uroda']
                zber.zisk = data['zisk']
                zber.cyklus = int(request.POST.get('cyklus'))
                zber.save()
                cyklus = Cyklus.objects.get(id=cyklus_id)
                cyklus.zber_id = zber.id
                cyklus.save()
                return HttpResponseRedirect('/sprava/cast/' + cast_id)
        else:
            form = NovyZberForm()
        return render(request, 'spravaPoli/novyZber.html', {'form': form, 'cast_id': cast_id, 'cyklus_id': cyklus_id})