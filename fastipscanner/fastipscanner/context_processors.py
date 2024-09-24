from .app_info import APP_NAME, VERSION


def app_info(request):
    return {
        "APP_NAME": APP_NAME,
        "VERSION": VERSION,
    }
