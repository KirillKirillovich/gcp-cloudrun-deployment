# gcp-cloudrun-deployment

### docker image usage:
1) Create image:
```
docker build -t flask-logger-app .
```
2) Run container with image
```
 docker run -d -p 8000:8000 flask-logger-app
 ```

### Cloud Scheduler usage: