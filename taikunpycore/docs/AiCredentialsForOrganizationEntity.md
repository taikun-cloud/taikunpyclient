# AiCredentialsForOrganizationEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**AiType**](AiType.md) |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.ai_credentials_for_organization_entity import AiCredentialsForOrganizationEntity

# TODO update the JSON string below
json = "{}"
# create an instance of AiCredentialsForOrganizationEntity from a JSON string
ai_credentials_for_organization_entity_instance = AiCredentialsForOrganizationEntity.from_json(json)
# print the JSON string representation of the object
print(AiCredentialsForOrganizationEntity.to_json())

# convert the object into a dict
ai_credentials_for_organization_entity_dict = ai_credentials_for_organization_entity_instance.to_dict()
# create an instance of AiCredentialsForOrganizationEntity from a dict
ai_credentials_for_organization_entity_from_dict = AiCredentialsForOrganizationEntity.from_dict(ai_credentials_for_organization_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


