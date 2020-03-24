import os
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    UPLOAD_FOLDER = "image-file"
    CSRF_ENABLED = True
    DEBUG = False
    
    # Enter your API Key and Custom Classifier ID below
    API_KEY = "x7vuspVNdxWHSipjE9VL-VwqZpm-r1oe5nG1thRyZiil"
    CLASSIFIER_ID = "Short-classifier_1094263068"
