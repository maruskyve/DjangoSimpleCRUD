from . import forms
from . import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
import datetime
import os


class FileManager:
    @staticmethod
    def getMediaPath():
        return os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)

    @staticmethod
    def deleteMediaFile(filepath):
        try:
            os.remove(filepath)

            return True
        except Exception as e:
            print(e)

        return False


class TextsService:
    @staticmethod
    def createTexts(request):
        """
        Request method should be POST
        :param request:
        :return:
        """
        if request.method == "POST":
            rp = request.POST

            if rp['input_text'] != "" and rp['input_textarea'] != "":
                mT = models.Texts(input_text=rp['input_text'],
                                  input_radio=rp['input_radio'],
                                  input_select=rp['input_select'],
                                  input_textarea=rp['input_textarea'],
                                  date=str(datetime.datetime.now()))
                mT.save()
                return True

        return False

    @staticmethod
    def updateTexts(request, pk):
        """
        Request method should be POST
        :param request:
        :param pk:
        :return:
        """
        if TextsService.isATextsExists(request, pk):
            rp = request.POST
            models.Texts.objects.filter(id=pk).update(input_text=rp['input_text'],
                                                      input_radio=rp['input_radio'],
                                                      input_select=rp['input_select'],
                                                      input_textarea=rp['input_textarea'])
            return True

        return False

    @staticmethod
    def deleteATexts(request, pk):
        if TextsService.isATextsExists(request, pk):
            models.Texts.objects.filter(id=pk).delete()
            return True

        return False

    @staticmethod
    def selectAllTexts(request):
        if request.method == "GET":
            return models.Texts.objects.all()

        return False

    @staticmethod
    def selectATexts(request, pk):
        if TextsService.isATextsExists(request, pk):
            return models.Texts.objects.filter(id=pk).get()

        return False

    @staticmethod
    def isATextsExists(request, pk):
        return models.Texts.objects.filter(id=pk).exists()


class FilesService:
    """
    General -> (FILES_UPLOAD)
    DatabaseServices -> (CREATE, READ_ALL, READ_ONE, UPDATE, DELETE)
    Validation -> (IS_EXISTS)
    """

    @staticmethod
    def uploadFiles(request):
        """
        Request method should be POST
        :param request:
        :return:
        """
        if request.method == "POST":
            file = request.FILES['input_file']
            file_ext = str(file).split('.')[-1]
            filename = str(get_random_string(77) + '.' + file_ext)

            fss = FileSystemStorage()
            f_save = fss.save(filename, file)

            return {'input_file': fss.url(f_save).split('/')[-1],
                    'input_filepath': fss.url(f_save)}

        return False

    @staticmethod
    def createFiles(request, up_data=None):
        up_data = {} if up_data is None else up_data

        if request.method == "POST":
            mF = models.Files(input_file=up_data['input_file'],
                              input_filepath=up_data['input_filepath'],
                              date=str(datetime.datetime.now()))
            mF.save()
            return True

        return False

    @staticmethod
    def selectAllFiles(request):
        if request.method == "GET":
            return models.Files.objects.all()

        return False

    @staticmethod
    def selectAFiles(request, pk, val=False):
        if FilesService.isAFilesExists(request, pk):
            mF = models.Files.objects.filter(id=pk)
            if val:
                return mF.values()[0]
            return mF.get()

        return False

    @staticmethod
    def updateAFiles(request, pk):
        if request.method == "POST":
            mFVal = FilesService.selectAFiles(request, pk, val=True)

            # Delete current file with match pk from media
            FileManager.deleteMediaFile(os.path.join(FileManager.getMediaPath(),
                                                     mFVal.get('input_file')))
            up_data = FilesService.uploadFiles(request)  # Upload File
            models.Files.objects.filter(id=pk).update(  # Update model data
                input_file=up_data['input_file'],
                input_filepath=up_data['input_filepath']
            )

        return False

    @staticmethod
    def deleteAFiles(request, pk):
        if request.method == "GET":
            try:
                mediapath = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)
                filename = FilesService.selectAFiles(request, pk, val=True).get('input_file')
                filepath = os.path.join(mediapath, filename)
                FileManager.deleteMediaFile(filepath)
                models.Files.objects.filter(id=pk).delete()
            except Exception as e:
                print(e)

            return True

        return False

    # Files Validation
    @staticmethod
    def isAFilesExists(request, pk):
        return models.Files.objects.filter(id=pk).exists()
