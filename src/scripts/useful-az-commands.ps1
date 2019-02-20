#azure  scripts

#don't run this directly
return

#region functions
$functionAppName = 'footyscraper-func'
$rgName = 'devtest'

#try first:
func azure functionapp publish footyscraper-func

#if you get 'There was an error restoring dependencies.ERROR: cannot install <library> dependency:'
func azure functionapp publish $functionAppName --build-native-deps --no-bundler

#if after that you get the error:

<#Error running docker pull mcr.microsoft.com/azure-functions/python:2.0.12285.
output:

Error response from daemon: Get https://mcr.microsoft.com/v2/: net/http: request canceled while waiting for connection (Client.Timeout exceeded while awaiting headers)
#>

#then set your dns to use 8.8.8.8 and try again


#assign a managed service identity to this app
az functionapp identity assign -n $functionAppName -g $resourceGroup



# add application settings to this application (accessible vs os.environ.get('Secret')
az functionapp config appsettings set -n $functionAppName -g $resourceGroup `
    --settings "Secret=SecretValue"
#endregion

#region azure container registry & kubernetes
#login to azure container registry & push images
az acr login --name footycontainerreg

#view images
docker images 

#tag image
#example container name
$imageRepositoryName = 'azure-vote-front'
$azureContainerRegistryLoginServer = 'footycontainerreg.azurecr.io'
$azureContainerRegistryName = 'footycontainerreg'

docker tag $imageRepositoryName $azureContainerRegistryLoginServer/$imageRepositoryName:v1

docker push $azureContainerRegistryLoginServer/$imageRepositoryName:v1

#list uploaded repository
az acr repository list --name $azureContainerRegistryName --output table
#show tags
az acr repository show-tags --name $azureContainerRegistryName --repository $imageRepositoryName --output table

#create active directoy app registration
az ad sp create-for-rbac --skip-assignment
#{ #note I have renamed the below to 'footy-container-manager'
#  "appId": "1aa2680f-5857-4314-b781-e456bc0d5934",
#  "displayName": "azure-cli-2019-02-18-20-04-31",
#  "name": "http://azure-cli-2019-02-18-20-04-31",
#  "password": "0387687b-6fa6-466d-9333-a4e3222a8471",
#  "tenant": "72f988bf-86f1-41af-91ab-2d7cd011db47"
#}

#get container registry id
az acr show --resource-group footy-backend --name footycontainerreg --query "id" --output tsv
#/subscriptions/26a2e37c-6e7c-48cc-92f0-1620b388c43f/resourceGroups/footy-backend/providers/Microsoft.ContainerRegistry/registries/footycontainerreg

#set app registration active directory to have pull access on registry using above Ids
az role assignment create --assignee 1aa2680f-5857-4314-b781-e456bc0d5934  `
    --scope /subscriptions/26a2e37c-6e7c-48cc-92f0-1620b388c43f/resourceGroups/footy-backend/providers/Microsoft.ContainerRegistry/registries/footycontainerreg `
    --role acrpull

# the below command will create the kubernetes cluster
#note service principal is appId from above 
#note client secret is password from above
az aks create --resource-group footy-backend --name footy-kubernetes --node-vm-size 'Standard_B2s' --node-count 3 --service-principal '1aa2680f-5857-4314-b781-e456bc0d5934' --client-secret '0387687b-6fa6-466d-9333-a4e3222a8471' --generate-ssh-keys

<#
{
  "aadProfile": null,
  "addonProfiles": null,
  "agentPoolProfiles": [
    {
      "count": 3,
      "maxPods": 110,
      "name": "nodepool1",
      "osDiskSizeGb": 30,
      "osType": "Linux",
      "storageProfile": "ManagedDisks",
      "vmSize": "Standard_B2s",
      "vnetSubnetId": null
    }
  ],
  "dnsPrefix": "footy-kube-footy-backend-26a2e3",
  "enableRbac": true,
  "fqdn": "footy-kube-footy-backend-26a2e3-5e176937.hcp.centralus.azmk8s.io",
  "id": "/subscriptions/26a2e37c-6e7c-48cc-92f0-1620b388c43f/resourcegroups/footy-backend/providers/Microsoft.ContainerService/managedClusters/footy-kubernetes",
  "kubernetesVersion": "1.9.11",
  "linuxProfile": {
    "adminUsername": "azureuser",
    "ssh": {
      "publicKeys": [
        {
          "keyData": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDb3pQHbLWuxMU+OpDS/LM98ww7EGk++qIZnxEWW760UMoSjfSg4cZwI8Wts6GLWzI4+noJkRHUlXH80+w07rZaQSK00l5jrzQD95EWIVB8Rwz0MY9NpexS64EWpuIfS+p5d5wkfjn2CiBDmO3BmGZQrXe1BEAievgpYG4FE/GRAdCv9gAZTsP1BHOMyUm20x4V/WL7gZhqbppUKzGyBbENseiW66TcUDOTRE8WXFnsvUWQj/YPUtpbxa8+Tj+QUuxUqgjIVSCCtQzRYF70+bxHT35i594h/LA/wjCfpzukXq81il+sUJWovq3HQHMEk8nEm8SQsLoOok4++HG3c4Pd"
        }
      ]
    }
  },
  "location": "centralus",
  "name": "footy-kubernetes",
  "networkProfile": {
    "dnsServiceIp": "10.0.0.10",
    "dockerBridgeCidr": "172.17.0.1/16",
    "networkPlugin": "kubenet",
    "networkPolicy": null,
    "podCidr": "10.244.0.0/16",
    "serviceCidr": "10.0.0.0/16"
  },
  "nodeResourceGroup": "MC_footy-backend_footy-kubernetes_centralus",
  "provisioningState": "Succeeded",
  "resourceGroup": "footy-backend",
  "servicePrincipalProfile": {
    "clientId": "1aa2680f-5857-4314-b781-e456bc0d5934",
    "secret": null
  },
  "tags": null,
  "type": "Microsoft.ContainerService/ManagedClusters"
}
#>

#ensure you have aks cli
az aks install-cli

#add credentials to your local
az aks get-credentials --resource-group footy-backend --name footy-kubernetes

# see node status
kubectl get nodes

#get login server name of registry created before
az acr list --resource-group footy-backend --query "[].{acrLoginServer:loginServer}" --output table

# AcrLoginServer
# ----------------------------
# footycontainerreg.azurecr.io

#apply, this will push image 
kubectl apply -f .\azure-vote-all-in-one-redis.yaml

#watch till public IP gets applied
kubectl get service azure-vote-front --watch

#view dashboard
az aks browse --resource-group footy-backend --name footy-kubernetes

#NOTE, I needed to go to https://blog.tekspace.io/kubernetes-dashboard-remote-access/ and follow instructions in order to be able to view this
<#
create yaml file kube-dashboard-access.yaml

apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: kubernetes-dashboard
  labels:
    k8s-app: kubernetes-dashboard
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: kubernetes-dashboard
  namespace: kube-system

kubectl create -f kube-dashboard-access.yaml

#>




#note I couldn't 

#endregion