# gcp-cloudrun-deployment

Usage:
1) Create image:
```
docker build -t flask-loger-app .
```
2) Run container with image
```
 docker run -d -p 8000:8000 flask-loger-app
 ```