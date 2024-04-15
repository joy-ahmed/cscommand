from django.apps import apps


def get_all_custom_models():
    default_models = ['ContentType', 'LogEntry',
                      'Session', 'Group', 'Permission', 'User']
    # try to get all the apps
    models = []
    for model in apps.get_models():
        # ignore default models
        if model.__name__ not in default_models:
            models.append(model.__name__)

    return models
