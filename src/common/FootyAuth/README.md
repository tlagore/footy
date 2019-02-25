Key Vault Manager

Any of the KeyManagers expects a config dicctionary with the following parameters:

use get_secret(secret_name) to get the secret from key vault

MSIKeyManager uses MSI - currently does not work locally or in prod but will when kubernetes pods have MSI

CertKeyManager - requires CLIENT_ID, TENANT_ID, THUMBPRINT, KV_URI, PKEY_FILE

AppKeyManager requires APP_SECRET, CLIENT_ID, TENANT_ID, KV_URI

```
{
  "TENANT_ID" : "<azure tenant (directory) id to which the client service principal belongs>",
  "CLIENT_ID" : "<azure client id of the client service principal, also called application id>",
  "THUMBPRINT" : "<thumbprint of the client cert>",
  "KV_URI" : "<uri to the key vault holding the secrets>",
  # this file must be downloaded from the keyvault manually for local development
  # DO NOT COMMIT THIS FILE TO VERSION CONTROL. If you name it <name>.pem .gitignore will ignore it
  "PKEY_FILE" : "<private key file>.pem",
  "APP_SECRET": os.environ.get("<Location-of-footy-app-secret>")
}
```

