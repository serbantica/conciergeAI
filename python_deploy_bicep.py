import os
from dotenv import load_dotenv
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
import json

# Load environment variables
load_dotenv()

subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group = os.getenv("AZURE_RESOURCE_GROUP")
location = os.getenv("AZURE_LOCATION")
bicep_file_path = os.getenv("AZURE_BICEP_FILE")
params_file_path = os.getenv("AZURE_PARAMETERS_FILE")

# Auth with Azure CLI
credential = AzureCliCredential()
resource_client = ResourceManagementClient(credential, subscription_id)

# Load parameters
with open(params_file_path, 'r') as f:
    parameters_dict = json.load(f)["parameters"]
    parameters = {k: {"value": v["value"]} for k, v in parameters_dict.items()}

# Deploy Bicep
with open(bicep_file_path, 'r') as f:
    print(f"Deploying: {bicep_file_path} to resource group: {resource_group}")

deployment_result = resource_client.deployments.begin_create_or_update(
    resource_group,
    "llm-concierge-deployment",
    {
        "location": location,
        "properties": {
            "mode": "Incremental",
            "template": None,
            "templateLink": None,
            "parameters": parameters,
            "templateContent": f.read(),
        },
    }
).result()

print("✅ Deployment complete:", deployment_result.properties.provisioning_state)