$subid = "26a2e37c-6e7c-48cc-92f0-1620b388c43f" 
$vaultName = "footkv"

Select-AzSubscription -SubscriptionId $subid
$vaultResourceId = (Get-AzKeyVault -VaultName $vaultName).ResourceId
$vault = Get-AzResource –ResourceId $vaultResourceId -ExpandProperties
$vault.Properties.TenantId = (Get-AzContext).Tenant.TenantId
$vault.Properties.AccessPolicies = @()
Set-AzResource -ResourceId $vaultResourceId -Properties $vault.Properties