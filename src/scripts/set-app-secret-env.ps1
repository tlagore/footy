$sec = az keyvault secret show --vault-name footkv --name FootyAppSecet
$secretvalue = ($sec | ConvertFrom-Json).value

[System.Environment]::SetEnvironmentVariable("FOOTY_APP_SECRET", $secretvalue, "Machine")
