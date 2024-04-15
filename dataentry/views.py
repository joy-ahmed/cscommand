from django.shortcuts import render
from django.apps import apps

from .utils import get_all_custom_models

# Create your views here.


def import_data(request):
    if request.method == 'POST':
        pass
    else:
        new_models = get_all_custom_models()
        print(new_models)
    # get all models associated with dataentry app
    return render(request, 'import_data.html', {'models': new_models})
