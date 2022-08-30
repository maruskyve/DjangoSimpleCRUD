from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from . import models, forms
from . import services

# Create your views here.

crud_path = "crud.html"
text_path = "texts.html"
text_edit_path = "texts_update.html"
files_path = "files.html"
files_edit_path = "files-update.html"


def view_crud(request):
    template = loader.get_template(crud_path)
    context = {}

    if request.method == "POST":
        rp = request.POST

        if rp['form'] == 'create_texts':
            services.TextsService.createTexts(request)
            # Recommended to use below reverse() to avoid form resubmission
            return HttpResponseRedirect(reverse('view_crud'))

        if rp['form'] == 'create_files':
            upload = services.FilesService.uploadFiles(request)
            services.FilesService.createFiles(request, upload)
            return HttpResponseRedirect(reverse('view_crud'))

    return HttpResponse(template.render(context))


# Texts

def view_texts(request):
    template = loader.get_template(text_path)
    context = {'request': request}

    context.update({'texts': services.TextsService.selectAllTexts(request)})

    return HttpResponse(template.render(context))


def view_texts_update(request, pk):
    template = loader.get_template(text_edit_path)
    context = {'request': request}

    # Check if model exists or not using their pk
    if services.TextsService.isATextsExists(request, pk):
        context.update({'texts': services.TextsService.selectATexts(request, pk)})
    else:
        return HttpResponseRedirect(reverse('view_texts'))

    if request.method == "POST":
        rp = request.POST

        if rp['form'] == "update_texts":
            services.TextsService.updateTexts(request, rp['id'])

            return HttpResponseRedirect(reverse('view_texts_update', kwargs={'pk': rp['id']}))

    return HttpResponse(template.render(context))


# Files

def view_files(request):
    template = loader.get_template(files_path)
    context = {'files': services.FilesService.selectAllFiles(request)}

    return HttpResponse(template.render(context))


def view_files_update(request, pk):
    template = loader.get_template(files_edit_path)
    context = {}

    # Check if model exists or not using their pk
    if services.FilesService.isAFilesExists(request, pk):
        context.update({'files': services.FilesService.selectAFiles(request, pk, val=False)})
        # print(services.FilesService.selectAFiles(request, pk))
    else:
        return HttpResponseRedirect(reverse('view_files'))

    if request.method == "POST":
        rp = request.POST

        if rp['form'] == "update_files":
            services.FilesService.updateAFiles(request, pk)
            return HttpResponseRedirect(reverse('view_files_update', kwargs={'pk': pk}))

    return HttpResponse(template.render(context))


# Independent views
def delete_texts(request, pk):
    if services.TextsService.deleteATexts(request, pk):
        # Use below redirect to previous page
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def delete_files(request, pk):
    if services.FilesService.deleteAFiles(request, pk):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
