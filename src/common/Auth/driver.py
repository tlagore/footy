from auth.auth import KeyManager

#usage
kv = KeyManager()
print(kv.get_secret("<secret_name>"))