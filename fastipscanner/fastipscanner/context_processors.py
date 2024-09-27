from .app_info import APP_DISPLAY_NAME, VERSION


def app_info(request):
    return {
        "APP_NAME": APP_DISPLAY_NAME,
        "VERSION": VERSION,
    }
