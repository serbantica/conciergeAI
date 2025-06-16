param name string
param image string
param location string
param envVars object
param managedEnvName string


resource containerApp 'Microsoft.App/containerApps@2023-05-01' = {
  name: name
  location: location
  properties: {
managedEnvironmentId: resourceId('Microsoft.App/managedEnvironments', managedEnvName)
    configuration: {
      activeRevisionsMode: 'Single'
      ingress: {
        external: true
        targetPort: 8000
      }
      registries: [
        {
          server: 'myregistry.azurecr.io'
          username: 'ACR_USERNAME'
          passwordSecretRef: 'acrPassword'
        }
      ]
      secrets: [
        {
          name: 'acrPassword'
          value: 'YOUR_PASSWORD'
        }
      ]
      environmentVariables: [
        for key in envVars: {
          name: key
          value: envVars[key]
        }
      ]
    }
    template: {
      containers: [
        {
          name: name
          image: image
        }
      ]
      scale: {
        minReplicas: 0
        maxReplicas: 3
        rules: [
          {
            name: 'http-scaler'
            custom: {
              type: 'http'
              metadata: {
                concurrentRequests: '50'
              }
            }
          }
        ]
      }
    }
  }
}
