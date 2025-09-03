MCP Server Deployment on Google App Engine
This document provides step-by-step instructions to deploy the provided MCP server on Google App Engine.

Files
The following files are required for deployment:

main.py: The Python Flask application code.

requirements.txt: A list of Python libraries the server needs.

app.yaml: The configuration file for Google App Engine.

Prerequisites
Google Cloud Account: You need an active Google Cloud account with billing enabled.

Google Cloud SDK: Install the Google Cloud SDK on your local machine.

Python: Python 3.9 or newer should be installed.

Text Editor: Any text editor to create and save the files above.

Step 1: Set up your Google Cloud Project
Create a new Google Cloud Project or select an existing one.

Open a terminal or command prompt.

Authenticate your Google Cloud SDK by running:

gcloud auth login

Set your project ID:

gcloud config set project YOUR_PROJECT_ID

(Replace YOUR_PROJECT_ID with your actual project ID).

Enable the App Engine Admin API for your project.

Step 2: Create the Files
Ensure the three files (main.py, requirements.txt, and app.yaml) are saved in the same directory on your computer.

Step 3: Deploy to Google App Engine
Open your terminal and navigate to the directory where you saved the files.

Run the following command to deploy your application:

gcloud app deploy

You will be prompted to choose a region and confirm the deployment. Type Y and press Enter. The deployment process may take a few minutes.

Step 4: Test the Deployed Server
Once the deployment is complete, Google Cloud will provide you with a URL for your service, typically in the format https://YOUR_PROJECT_ID.REGION_ID.r.appspot.com.

You can test the endpoint using a curl command from your terminal. This command mimics the request that Intercom will send, with the flattened JSON parameters.

curl --location 'https://YOUR_PROJECT_ID.REGION_[ID.r.appspot.com/v2/iw/check-deeplink](https://ID.r.appspot.com/v2/iw/check-deeplink)' \
--header 'Content-Type: application/json' \
--data '{
    "db_name": "NDTVProfit",
    "user_id": "eb50c9bb-fac4-44c7-b97d-36ab374c5ef8",
    "campaign_id": "68b2cd88c85096a0c1603cf0",
    "date": "2025-08-30",
    "region":"DC1"
}'

Remember to replace YOUR_PROJECT_ID and REGION_ID with your specific values. The server should return the expected JSON response from the external API.

This setup ensures that your server is ready to integrate with Intercom, accepting the required flattened schema and forwarding the request as a nested object to the final API endpoint.