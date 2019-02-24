$tenantId = (Get-AzContext).Tenant.TenantId
$applicationId = "2795bb93-a063-4c9e-a7cb-ec9a66f0efc6"
$certThumbprint = "233e44576fed0a3993db9253f6f8b5043184c69d"
# Test authenticating as Service Principal to Azure

Login-AzAccount `
-ServicePrincipal `
-TenantId $tenantId `
-ApplicationId $applicationId `
-CertificateThumbprint $certThumbprint