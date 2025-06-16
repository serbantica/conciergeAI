@secure()
param acrPassword string

@description('Azure Container Registry username')
param acrUsername string = 'YOUR_USERNAME'

@description('Azure Container Apps environment name')
param managedEnvName string

targetScope = 'resourceGroup'

@description('Deploy orchestrator (FastAPI)')
param deployOrchestrator bool = true

@description('List of agents to deploy')
param agentList array = ['calendar', 'todo', 'financial', 'knowledge', 'fun', 'social', 'pager', 'web', 'search', 'code']

@description('Location of the deployment')
param location string = resourceGroup().location

@description('Name of the managed environment for Container Apps')
param managedEnvName string = 'concierge-env'

// Module: Key Vault
module keyVault 'modules/keyVault.bicep' = {
  name: 'kvModule'
  params: {
    location: location
  }
}

// Module: Orchestrator API (Container App)
module orchestrator 'modules/containerApp.bicep' = if (deployOrchestrator) {
  name: 'orchestratorApp'
  params: {
    name: 'concierge-api'
    image: 'myregistry.azurecr.io/orchestrator:latest'
    managedEnvName: managedEnvName
    location: location
    envVars: {
      'ENV': 'dev'
      'KEY_VAULT_URI': keyVault.outputs.vaultUri
    }
        acrUsername: acrUsername
    acrPassword: acrPassword
  }
}

// Loop through agent modules
@for agent in agentList: module agentApp 'modules/containerApp.bicep' = {
  name: 'agent-${agent}'
  params: {
    name: 'agent-${agent}'
    image: 'myregistry.azurecr.io/${agent}:latest'
    managedEnvName: managedEnvName
    location: location
    envVars: {
      'ENV': 'dev'
      'KEY_VAULT_URI': keyVault.outputs.vaultUri
    }
    acrUsername: acrUsername
    acrPassword: acrPassword
  }
}
