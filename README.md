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

1) Go to the <strong>Google Cloud Console</strong>. <br>

2) Navigate to <strong>Cloud Scheduler</strong>. <br>

3) Click <strong>Create Job</strong>. <br>

4) Fill out the job details: <br>

    Name: your_scheduler_name. <br>
    Frequency: Set the frequency using a cron expression (e.g., */5 * * * * for every 5 minutes). <br>
    Timezone: Select the appropriate timezone.

5) Under Target, choose HTTP.

6) In the URL field, enter the URL of your Cloud Run service, specifying the /scheduler endpoint. For example: https://your_app_ip/scheduler <br>

7) Set the HTTP Method to POST.

8) Add the Body of the request. This is where you send the payload. Enter your JSON payload in the Body field. Example:
```
{
  "key1": "value1",
  "key2": "value2"
}
```
### HTTP headers have to include:
```
Content-Type: application/json
```
9) Click Create to finish setting up the job.