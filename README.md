# Django 2 example app for OpenShift (Kubernetes)

## Dominate Pizza, the site for pizza lovers
Using Django 2, Gunicorn and Django Rest Framework.

### Serving static content
The application will be served in OpenShift by Gunicorn. 
By default the Python S2I container will run the Django collect static command (change behavior with *DISABLE_COLLECTSTATIC*).
Since those files cannot be placed on persistent volume during build and these are not served by the development Django server, you need to go for one of these options:
- Make Gunicorn serve */static*. Done here by using WhiteNoise. If used in production, add a cache layer (Nginx, CDN...).
- Overwrite the default Python S2I *build* action hook to collect static files (default is in *assemble* step) to place files on a shared mounted PV with RWX access between the Django instance(s) and a Nginx instance.

### OpenShift settings

#### Common environment variables to overwrite defaults:
 - DEBUG
 - DJANGO_LOG_LEVEL
 - DJANGO_SECRET_KEY
 - OPENSHIFT_REPO_DIR
 
 #### Deployment
 When deploying a Python application in OpenShift, the DeploymentConfig created uses the *Rolling* strategy which is a risk since OpenShift automatically calls Django's *migrate* when starting the container. There for it's safer to change the strategy to *Recreate*.
 
 #### Jaeger Tracing
 The Istio/Service Mesh Operator will deploy a Jaeger agent per node in a cluster rather than expect each app to have a Jaeger sidecar.
 A Jaeger client will not be able to reach that agent as 'localhost', there for the DeployemntConfig of the app must be fed the real IP of the host on which the agent can be reached.
 ```yaml
 spec:
      containers:
        - env:
            - name: JAEGER_AGENT_HOST
              valueFrom:
                fieldRef:
                  fieldPath: status.hostIP
```
 
 ### Development
 If running locally (127.0.0.1) and setting DEBUG to True, the Django Debug Toolbar will be shown.
 
 
