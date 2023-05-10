from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Fakultas
from .forms import FakultasForm


# Create your views here.
def indexView(request):
    fakultas = Fakultas.objects.all()

    return render(request, "fakultas/index.html", {"fakultas": fakultas})


def detailView(request, fakultas_id):
    try:
        fakultas = Fakultas.objects.get(pk=fakultas_id)
        context = {"fakultas": fakultas}
    except Fakultas.DoesNotExist:
        raise HttpResponse("fakultas tidak ditemukan !!!")

    return render(request, "fakultas/detail.html", context)


def createView(request):
    if request.method == "POST":
        form = FakultasForm(request.POST)

        if form.is_valid():
            nama_fakultas = form.cleaned_data["nama_fakultas"]
            prodi = form.cleaned_data["prodi"]
            Fakultas.objects.create(
                nama_fakultas=nama_fakultas,
                prodi=prodi,
            )

            messages.success(request, "Data berhasil disimpan!!!")
            return redirect("akademik:index")
    else:
        form = FakultasForm()

    return render(request, "fakultas/form.html", {"form": form})


def updateView(request, fakultas_id):
    try:
        fakultas = Fakultas.objects.get(pk=fakultas_id)
    except Fakultas.DoesNotExist:
        raise HttpResponse("Fakultas tidak ditemukan!!!")

    if request.method == "POST":
        form = FakultasForm(request.POST)
        if form.is_valid():
            fakultas.nama_fakultas = form.cleaned_data["nama_fakultas"]
            fakultas.prodi = form.cleaned_data["prodi"]
            fakultas.save()

            messages.success(request, "Data berhasil diubah!!!")
            return redirect("akademik:index")
    else:
        form = FakultasForm(
            initial={"nama_fakultas": fakultas.nama_fakultas, "prodi": fakultas.prodi}
        )

    return render(request, "fakultas/form.html", {"form": form})


def deleteView(request, fakultas_id):
    try:
        fakultas = Fakultas.objects.get(pk=fakultas_id)
        fakultas.delete()

        messages.success(request, "Data berhasil dihapus!!!")
        return redirect("akademik:index")

    except Fakultas.DoesNotExist:
        raise ("Fakultas tidak ditemukan !!!")
