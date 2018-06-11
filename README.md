# TWI_to_FB
Scheduled Post Twitter User Timeline Tweets To Facebook Page

## LIBRARIES USED
* TWEEPY  
* APSCHEDULER  
* FACEBOOK-SDK
  
## USAGE
### PREREQUISITES
* python 3.4 or above

### CONFIGURATION
* Create your bot and Get your telegram bot token from [BotFather](https://core.telegram.org/bots#botfather)
* Create an app on facebook [Facebook developers](https://developers.facebook.com/apps/)   
* Get page access token of facebook page by following this [StackOverflow Link](https://stackoverflow.com/a/43570120)
* Create an app on twitter [https://apps.twitter.com]
* Get Consumer key , Consumer secret, Access key and Access secret of your twitter app
* Fill the fields in config.ini ,put user name of twitter account in handle field
* If you are hosting this script on Redhat Openshift Online also fill the persistent_mount_point field else leave it empty
* After all these steps you are all set

### RUNNING ON LOCAL PC
* run pip install -r requirements.txt in console/cmd/powershell in the directory of project
* run app.py script
* enjoy

### HOSTING ON OPENSHIFT ONLINE
* edit the config.ini file
* save all the files in a repository on github  
* create an account on [REDHAT OPENSHIFT ONLINE](https://www.openshift.com)
* select the location of your server 
* wait for some time till you recieve confirmation
* after recieving confirmation, login and create new application
* select python 3.4 or above
* select name and everything
* enter the url of the github repository
* you can also use private repository , by adding authentication secret in build config
* wait for application to start
* enjoy

#### REBUILDING PROJECT ON OPENSHIFT ONLINE  
when you want to rebuild your project  

* first of all go to deployments and select the latest deployment
* downscale the no of pods to 0 and wait for it to happen
*  **IMPORTANT** go to deployment configuration and detach the storage. A deployment will start, let it finish
* Go to builds, select name and click on start build
* After finishing build a deployment will start, let it finish
* Go back to deployment configuration and add storage with same mount point as previous and wait for a new deployment
* After deployment finishes, go to deployments. Select latest and scale the pod to 1.  

* **YOU CAN REMOVE YOUR GITHUB REPOSITORY BUT MAKE SURE TO RECREATE IT WHEN REBUILDING YOUR PROJECT**  