# flask_5_tailwind

## Video Creation
This past summer I went on a trip to Lake Placid and took a video overlooking the Adirondack Mountains and Lake Placid Lake. The video was recorded at one of the High Peaks of the Adirondack Mountains with the elevation at 4,867′.

## Cloud CDN and Video Hosting Setup
1. Once logged into Microsoft Azure, to go **`Storage accounts`**.
2. Click `Create`, under `Project details` create a new `Resource group`. Under `Instance details` create a new `Storage account name`. Then click `Create`.
3. Navigate back to the **`Storage accounts`** page, and click on the storage account you just created, click `Overview` from the navigation menu on the left-hand side, and under Properties click `Security`. Ensure the following is **`Enabled`**: `Secure transfer required, Allow Blob anonymous access, Allow storage account key access`. Click `Save`.
4. In the same navigation menu as Overview, under `Data Storage` click **`Containers`**. Click on `Create` and create a name and under `Anonymous access level` use the drop down to select `Containner (anonymous read access for containers and blob`, then click `Create`.
5. Again navigate to the menu and under `Security + networking` click **`Front Door and CDN`**. Under `New Endpoint` and change the service type to `Azure CDN`. Create a `Profile name` and `Endpoint name`. Change the `Query string caching behavior` to `Ignore query string` and then click `Create`.
6. Navigate back to your storage account that you will be using and click `Upload`. Upload a video of your choice, however ensure the video's lenght is less than 60 seconds and select the container you created. Then click `Upload`.
7. Next, go back to your storage account and click `Front Door and CDN`, then click the link under `Host name` and then open the link associated with `Endpoint hostname` in a new tab. The endpoint hostname should end in `.azureedge.net`.
8. Lastly, go back to the storage account you are working with and click on `Containers`, then the container you just created. There the video you uploaded will be displayed. Click on the the video's name and copy the URL to clipboard. Go to the tab you opened with the endpoint hostname, and type `/` after the `.net` and paste the URL you had copied on to your clipboard after the "/" and hit enter. The video you had uploaded should then play. This new URL will be used in the base.html file for the source.

## Steps to deploying the Flask app to Azure
1. In your Google Cloud Shell terminal, install Azure CLI by typing in this command `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash` and hit enter.
2. Then type `az`and hit enter to test if Azure was intalled.
3. After that type `az login --use-device-code` to log in. After you hit enter a link will be provided with an authentication code, copy the authentication code, click the link, sign in with your emial, and paste the authentication code.
4. Go back into the terminal on Cloud Shell and redeem your azure student subscription ID by the command ```az account list --output table ``` and hit enter. Ensure you are using the correct subscription.
5. If you are not using the correct subscription, to change into the subscription id, use the command ```az account set --subscription <type your subscriptionid that you obtained above> ``` 
6. Go back to Cloud Shell, in the terminal type the command, ```az webapp --resource-group <groupname> --name <app-name> --runtime <PYTHON : 3.9 > --sku <B1> ```. A webapp is now created for your flask app.
7. Go to the Azure Website and on the Home page click **`App Services`**, then click app name. The link next to `Default domain` is the link for your application. Once you click the link, it'll direct you to your deployed flask app.

The link to my Flask app is https://amnasflaskapp.azurewebsites.net/ ,and you can see videos of the appliaction via desktop and mobile as well as screenshots of the app in the `Screenshots and Videos` folder above. 

## Observations and benefits of using a CDN and cloud deployment
A benefit of using a CDN and cloud deployment is everything is compartmentalized in an easy and accessible manner. Cloud deployment makes the process of deployment of an applications fast, seamless, and easy. CDNs also allow for end users to access content from different devices very easily and in a timely manner. For instance, when I was testing if the design was responsive using a mobile device, not only was the design compatible but the access time for the website was also very fast. 

## Challenges encountered
I only encountered one challenge and that was when uploading my video to the container. The video I had uploaded was in .mov format and when testing the link out, when I would add the second part of the url after .net, it would automatically download to my computer instead of the video playing from the link. Therefore, I converted my video from .mov to .mp4 and everything worked seamlessly after that. 
