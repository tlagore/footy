$enc = [system.Text.Encoding]::UTF8
$secret = Get-AzKeyVaultSecret -SecretName FootyCertPK -VaultName footkv

$bytes = $enc.GetBytes($secret.SecretValueText)
$bytes | Set-Content .\shloobydoo.pem -Encoding Byte
 