from footy_auth.footy_auth import AppKeyManager, CertKeyManager

print("AppKeyManager test (app secret authentication)")
akm = AppKeyManager()
print(akm.get_secret("MongoDBPass"))

#usage
print("CertKeyManager test (private key authentication)")
kv = CertKeyManager()
print(kv.get_secret("MongoDBPass"))