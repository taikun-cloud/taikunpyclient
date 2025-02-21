# BackupCredentialsForOrganizationEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_credential_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**is_infra** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.backup_credentials_for_organization_entity import BackupCredentialsForOrganizationEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BackupCredentialsForOrganizationEntity from a JSON string
backup_credentials_for_organization_entity_instance = BackupCredentialsForOrganizationEntity.from_json(json)
# print the JSON string representation of the object
print(BackupCredentialsForOrganizationEntity.to_json())

# convert the object into a dict
backup_credentials_for_organization_entity_dict = backup_credentials_for_organization_entity_instance.to_dict()
# create an instance of BackupCredentialsForOrganizationEntity from a dict
backup_credentials_for_organization_entity_from_dict = BackupCredentialsForOrganizationEntity.from_dict(backup_credentials_for_organization_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


