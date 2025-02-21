# OperationCredentialsForOrganizationEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_credential_id** | **int** |  | 
**name** | **str** |  | 
**is_default** | **bool** |  | 

## Example

```python
from taikunpycore.models.operation_credentials_for_organization_entity import OperationCredentialsForOrganizationEntity

# TODO update the JSON string below
json = "{}"
# create an instance of OperationCredentialsForOrganizationEntity from a JSON string
operation_credentials_for_organization_entity_instance = OperationCredentialsForOrganizationEntity.from_json(json)
# print the JSON string representation of the object
print(OperationCredentialsForOrganizationEntity.to_json())

# convert the object into a dict
operation_credentials_for_organization_entity_dict = operation_credentials_for_organization_entity_instance.to_dict()
# create an instance of OperationCredentialsForOrganizationEntity from a dict
operation_credentials_for_organization_entity_from_dict = OperationCredentialsForOrganizationEntity.from_dict(operation_credentials_for_organization_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


