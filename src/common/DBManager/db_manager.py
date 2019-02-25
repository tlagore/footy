from footy_auth.footy_auth import AppKeyManager

akm = AppKeyManager()
print(akm.get_secret("MongoDBPass"))
