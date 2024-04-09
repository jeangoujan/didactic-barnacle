import os


class Playwright:
    PAGE_VIEWPORT_SIZE = {'width': 1382, 'height': 934} # Надо изменить на fullscreen
    ENV = os.getenv('ENV', default='stage')
    BROWSER = os.getenv('BROWSER', default='chrome')
    IS_HEADLESS = os.getenv('HEADLESS', default=False)
    SLOW_MO = int(os.getenv('SLOW_MO')) if os.getenv('SLOW_MO') is not None else 50
    LOCALE = 'en-US'
