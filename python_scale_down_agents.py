import os
from dotenv import load_dotenv
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient

from azure.mgmt.appcontainers import ContainerAppsAPIClient


# This script scales down all Azure Container Apps in a specified resource group to 0 replicas.
# It uses the Azure SDK for Python to authenticate and manage resources.
# Ensure you have the required packages installed:  
# pip install azure-identity azure-mgmt-resource azure-mgmt-web azure-mgmt-appcontainers python-dotenv
# Import necessary libraries


# Load environment
load_dotenv()
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group = os.getenv("AZURE_RESOURCE_GROUP")

# Authenticate
credential = AzureCliCredential()
container_client = ContainerAppsAPIClient(credential, subscription_id)

# List all container apps in the resource group
apps = container_client.container_apps.list_by_resource_group(resource_group)

# Scale each app to 0
for app in apps:
    print(f"🔧 Scaling down {app.name}...")
    container_app = container_client.container_apps.get(resource_group, app.name)

    # Set scale.minReplicas = 0
    container_app.template.scale.min_replicas = 0

    # Apply the update
    poller = container_client.container_apps.begin_create_or_update(
        resource_group, app.name, container_app
    )
    poller.result()
    print(f"✅ {app.name} scaled to 0.")

print("🎉 All container apps scaled down to 0 replicas.")