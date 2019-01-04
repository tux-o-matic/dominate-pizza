# Django 2 example app for OpenShift (Kubernetes)

## Dominate Pizza, the site for pizza lovers
Using Django 2, Gunicorn and Django Rest Framework.

### Serving static content
The application will be served in OpenShift by Gunicorn. 
By default the Python S2I container will run the Django collect static command (change behavior with *DISABLE_COLLECTSTATIC*).
Since those files cannot be placed on persistent volume during build and these are not served by the development Django server, you need to go for one of these options:
- Make Gunicorn serve */static*. Done here by using WhiteNoise. For production you should add a cache layer (Nginx, CDN...).
- Run an Nginx container build with each new change to your static files or with a *PV* mounted and loaded with the files.

### OpenShift settings

#### Common environment variables to overwrite defaults:
 - DEBUG
 - DJANGO_LOG_LEVEL
 - DJANGO_SECRET_KEY
 - OPENSHIFT_REPO_DIR
 
 #### Deployment
 When deploying a Python application in OpenShift, the DeploymentConfig created uses the *Rolling* strategy which is a risk since OpenShift automatically calls Django's *migrate* when starting the container. There for it's safer to change the strategy to *Recreate*.
 
 ### Development
 If running locally (127.0.0.1) and setting DEBUG to True, the Django Debug Toolbar will be shown.
