import os


def pytest_generate_tests(metafunc):
    os.environ['DJANGO_SETTINGS_MODULE'] = "asd.settings"
