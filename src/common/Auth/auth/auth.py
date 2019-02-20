from azure.keyvault import KeyVaultClient, KeyVaultAuthentication, KeyVaultId
from azure.common.credentials import ServicePrincipalCredentials

def auth_callback(server, resource, scope):
    credentials = ServicePrincipalCredentials(
        client_id = '',
        secret = '',
        tenant = '72f988bf-86f1-41af-91ab-2d7cd011db47',
        resource = 'https://vault.azure.net'
    )

    token = credentials.token
    return token['token_type'], token['access_token']

client = KeyVaultClient(KeyVaultAuthentication(auth_callback))

secret_bundle = client.get_key('https://footkv.vault.azure.net/', 'MongoDBPass', KeyVaultId.version_none)