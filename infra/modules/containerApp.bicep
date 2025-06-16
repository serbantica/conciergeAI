param name string
param image string
param location string
param envVars object
param managedEnvName string
@secure()
param acrPassword string
param acrUsername string = 'YOUR_USERNAME'


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
        transport: 'auto'
      }
      secrets: [
        {
          name: 'acrPassword'
          value: acrPassword
        }
      ]
      registries: [
        {
          server: 'myregistry.azurecr.io'
          username: acrUsername
          passwordSecretRef: 'acrPassword'
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
