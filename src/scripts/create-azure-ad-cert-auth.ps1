#if (!(Get-Module -ListAvailable -Name Az)) {
#    Write-Host "This scritp requires module Requires module Az.Resources"
#    Write-Host "Use Install-Module Az"
#} 

$subid = "26a2e37c-6e7c-48cc-92f0-1620b388c43f" 
$context = (Get-AzContext)
if($context.Name -notlike "*$subid*"){
    Connect-AzAccount  -Subscription 26a2e37c-6e7c-48cc-92f0-1620b388c43f #-Tenant 601ec5fe-3c4e-4ba2-b15c-3ff7ad272a7e
}

$cert = New-SelfSignedCertificate -CertStoreLocation "Cert:\CurrentUser\My" -Subject "CN=footy-cert-prod" -KeySpec KeyExchange
$keyValue = [System.Convert]::ToBase64String($cert.GetRawCertData())

$sp = New-AzADServicePrincipal -DisplayName footyapp -CertValue $keyValue -EndDate $cert.NotAfter -StartDate $cert.NotBefore

for($i = 4; $i -gt 0; $i--){
    Write-Host "Sleeping $($i * 5) seconds"
    Sleep 5
}

New-AzRoleAssignment -RoleDefinitionName Contributor -ApplicationId $sp.ApplicationId
#    -CertValue $keyValue `
#    -EndDate $cert.NotAfter
#    -StartDate $cert.NotBefore

