import os
from dotenv import load_dotenv
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

# Load environment variables
load_dotenv()

subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group = os.getenv("AZURE_RESOURCE_GROUP")

# Authenticate using Azure CLI identity
credential = AzureCliCredential()
resource_client = ResourceManagementClient(credential, subscription_id)

# Confirm before deleting
confirm = input(f"⚠️ Are you sure you want to DELETE the entire resource group '{resource_group}'? (yes/no): ")
if confirm.lower() != 'yes':
    print("❌ Deletion cancelled.")
    exit(0)

# Delete resource group
print(f"🗑️ Deleting resource group: {resource_group} ...")
delete_poller = resource_client.resource_groups.begin_delete(resource_group)
delete_poller.result()  # waits until completion

print("✅ Resource group deleted successfully.")