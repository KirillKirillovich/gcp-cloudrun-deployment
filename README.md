# gcp-cloudrun-deployment

### docker image usage:
1) Create image:
```
docker build -t flask-logger-app .
```
2) Run container with image
```
 docker run -d -p 8080:8080 flask-logger-app
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


# Project workflows
## Including two workflows:
1) Creating environment and store GCP project data in secrets workflow:
```
gcp_environment_creator.yml
```
2) Deploying application to GCP with precreated github environment workflow:
```
gcp_cloud_run_deployment.yml
```

# Usage:
## Creating and store GCP project secrets and variables
### If you want use a GitHub Action to create a new environment that holds all your GCP project's secrets and variables, you have to do some steps. Most of the steps should be performed once when creating a new project.
```
gcp_environment_creator.yml
```
#### 1) Create an empty project in GCP (one-time step)
   - visit <strong>google cloud console</strong> and login to your account.
   - Create a new project: </br> 
        - <strong>select a project</strong> -> <strong>New project</strong>
        - Project name - name-of-the-project(copy id of the project for future usage)
        - Select the created project using the <strong>the selector in the upper left corner of the screen.</strong>
        - Lcoation - no organization
#### 2) Check if Service Usage API enabled on the project, without this service we will not be albe to use service account API (one-time step)
   - press on searchbar and look for <strong>'Service usage API'</strong> -> <strong>Enable</strong> if disabled
#### 3) Create Service Account manager to create and manage service accounts (one-time step)
   - click on <strong>burger on left side</strong> -> <strong>IAM & Admin</strong> -> <strong>Service Accounts</strong>
   - press <strong>create service account</strong>
   - fill up fields:
     - name - name of service account (for ex. 'projectname-serv-manager')
     - press <strong>create and continue</strong>
     - add four roles for managing and creating service account:
       - <strong>Service Account Admin</strong>(Create and manage service accounts. Will allow us to create a 'project-deployer' service account)
       - <strong>Project IAM Admin</strong>(Access and administer a project IAM policies. Gives us the ability to assign policec to the created service account)
       - <strong>Service Usage Admin</strong>(Ability to enable, disable, and inspect service states.Will give us the ability to manage the Services API. We need to enable such services as <strong>Google Cloud Run</strong>, <strong>Artifact Registry</strong>, etc)
       - <strong>Service account key admin</strong>(Create and manage (and rotate) service account keys. Ability to create JSON key for the created account)
     - press <strong>DONE</strong>
#### 4) Generate service account key and store it. (one-time step)
   - choose created 'projectname-serv-manager' -> <strong>actions</strong> -> <strong>manage keys</strong> -> select <strong>add key</strong> -> <strong>create neaw key</strong>(JSON)
   - open downloaded JSON key -> copy content -> past to github repo secret as SERVICE_ACCOUNT_MANAGER_KEY
#### 5) Setup github environment for the GCP project (workflow usage)
##### !!! IMPORTANT(YOU HAVE TO GENERATE Personal Access Token (PAT) AND ADD IT TO REPO SERCRETS LIKE 'PAT_TOKEN') PAT have include 'repo' and 'workflow' permissions<br> https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic. <br> (till expired step)
   - visit github repo -> <strong>Actions</strong> -> choose <strong>Setup github environment</strong> -> <strong>Run workflow</strong>, fields:
     - <strong>The GCP Project ID</strong> - input precraeated <strong>name-of-the-project id</strong> from first step.
     - <strong>The name of the GitHub environment to create</strong> - name of the GitHub environment (for ex. project-name-staging). Some rules there:
       - !!!name should include max 19 characters long.
       - lowercase letters.
      - <strong>Run workflow</strong> -> wait some minutes.
   - Now you can check Environments in github repo and you will see 'name-of-the-project-staging' with precreated secrets:
        - <strong>GCP_PROJECT_ID</strong> - id of the CGP project
        - <strong>GCP_REPO_ID</strong> - presetuped repo name for artifact regestry
        - <strong>GCP_SERVICE_ACCOUNT_DEPLOYER_KEY</strong> - key for the created service_account_deployer which has permissions for opperating <strong>Google Cloud Run</strong>, <strong>Artifact Regestry</strong>. This account will push Docker images to <strong>Artifact Regestry</strong> and deploy it to <strong>Google Cloud Run</strong>. <br>
### Deploying application to GCP with precreated github environment
```
gcp_cloud_run_deployment.yml
```
1) <strong>Start deployment workflow</strong>
   - visit github repo -> <strong>Actions</strong> -> choose <strong>Deploy app to Google Cloud Run</strong> -> <strong>Run workflow</strong>, fields:
     - environment of project - name of precreated github environment
     - image name to deploy - name of the image(will store image with this name in <strong>Artifacr Regestry</strong>)
     - region to deploy - set GCP region (for ex. europe-central2)<br> list with regions:<br>(https://cloud.google.com/compute/docs/regions-zones)
     - version of image - version of application (will store this version in <strong>artifact regestry</strong>(for ex. <strong>v1</strong>), by default will be <strong>'latest'</strong>)
     - <strong>Run workflow</strong> -> wait some minutes
2) <strong>Visit Cloud Run in GCP and check your app.</strong>