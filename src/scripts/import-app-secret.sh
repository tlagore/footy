#!/bin/bash
#requires jq and az lib
#brew install az
#brew install jq
export FOOTY_APP_SECRET=$(az keyvault secret show --vault-name footkv --name FootyAppSecret | jq -r '.value')