from django.conf import settings
from django.shortcuts import redirect, render
from django.core.management import call_command

from .utils import get_all_custom_models
from uploads.models import Upload

# Create your views here.


def import_data(request):
    new_models = None
    if request.method == 'POST':
        file_path = request.FILES.get('file')
        model_name = request.POST.get('model')
        # store data inside upload database table
        upload = Upload.objects.create(file=file_path, model_name=model_name)
        # relative path
        relative_path = upload.file.url
        base_url = settings.BASE_DIR
        # file absolute path
        file_abs_path = str(base_url) + str(relative_path)
        print(file_abs_path)
        # trigger import data command
        try:
            call_command('importdata', file_abs_path, model_name)
        except Exception as e:
            raise e
        return redirect('import-data')
    else:
        new_models = get_all_custom_models()
    # get all models associated with dataentry app
    return render(request, 'import_data.html', {'models': new_models})
