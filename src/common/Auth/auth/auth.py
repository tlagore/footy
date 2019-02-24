import requests
import os
import adal
from datetime import datetime
import json
import config

class KeyManager:
    def __init__(self, key_file=config.PKEY_FILE, client_id=config.CLIENT_ID, tenant_id=config.TENANT_ID, 
            kv_uri=config.KV_URI, thumbprint=config.THUMBPRINT):
        """KeyManager handles getting keys from keyvault"""
        #set initial expiry to epoch, if a key is requested it will force a token refresh
        self._token_expiry = datetime(1970, 1, 1, 0, 0)
        self._auth_context = adal.AuthenticationContext(f"{config.AUTH_URI}/{tenant_id}")
        self._oauth_token = None
        self._thumbprint = thumbprint
        self._client_id = client_id
        self._kv_uri = kv_uri
        self._key_file = key_file
        self._key = self.get_private_key()

    def get_private_key(self):
        """ read the private key from the supplied key file """
        with open(self._key_file , 'r') as pem_file:
            private_pem = pem_file.read()
        return private_pem

    def refresh_token(self):
        """refresh the oauth token"""
        try:
            token = self._auth_context.acquire_token_with_client_certificate(
                config.KV_RESOURCE_URI,
                self._client_id,
                self._key,
                self._thumbprint
            )

            #strip microseconds from expires on
            expStr = token["expiresOn"]
            expStr = expStr[:expStr.index('.')]
            expiry = datetime.strptime(expStr, '%Y-%m-%d %H:%M:%S')
            self._oauth_token = token["accessToken"]
        except Exception as ex:
            print(ex)
        
    def is_token_expired(self):
        """check to see if the token is expired"""
        return self._token_expiry < datetime.utcnow()      

    def get_secret(self, secret_name, secret_version = None):
        """ 
            Get a secret from the key vault. secret_version = None will return latest version 
            A failed call will return none
        """        
        if self.is_token_expired():
            self.refresh_token()
        
        val = None

        headers = {
            "Authorization" : f"Bearer {self._oauth_token}"
        }

        uri = f'{self._kv_uri}/secrets/{secret_name}/'
        query_params = f'?api-version={config.API_VERSION}'

        resp = requests.get(f'{uri}{query_params}', headers=headers)

        if(resp.status_code != 200):
            print("Error getting secret")
            print(f"Server returned status code: {resp.status_code}")
        else:
            data = json.loads(resp.text)
            val = data["value"]

        return val

## this works too, but requires us to have the secret. We have this stored in keyvault as well, could
## be a different way to do it instead of using oauth tokens. Store the secret as an environment variable
## for example
# def auth_callback(server, resource, scope):
#     credentials = ServicePrincipalCredentials(
#         client_id = '<client_id>',
#         secret = '<secret>',
#         tenant = '<tenant_id>',
#         resource = 'https://vault.azure.net'
#     )

#     token = credentials.token
#     return token['token_type'], token['access_token']

# client = KeyVaultClient(KeyVaultAuthentication(auth_callback))

# secret_bundle = client.get_secret('<kvuri>', '<secret>', KeyVaultId.version_none)


##with MSI, should work on instances
# credentials = MSIAuthentication(
#     resource='https://vault.azure.net'
# )

# key_vault_client = KeyVaultClient(
#     credentials
# )

# key_vault_uri = os.environ.get("<kv_uri>")

# secret = key_vault_client.get_secret(
#     key_vault_uri,  # Your KeyVault URL
#     "<secret_name>",      
#     "<secret_version>" # leave empty for latest version
# )