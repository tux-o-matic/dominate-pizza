# Django 2 example app for OpenShift

## Dominate Pizza, the site for pizza lovers
Using Django 2, Gunicorn and Django Rest Framework.

## OpenShift settings

Environment variables to overwrite defaults:
 - DEBUG
 - DJANGO_LOG_LEVEL
 - DJANGO_SECRET_KEY
 - OPENSHIFT_REPO_DIR
 
 If running locally (127.0.0.1) and setting DEBUG to True, the Django Debug Toolbar will be shown.