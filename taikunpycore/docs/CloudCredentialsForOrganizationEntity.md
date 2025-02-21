# CloudCredentialsForOrganizationEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**full_name** | **str** |  | 
**cloud_type** | [**CloudType**](CloudType.md) |  | 
**is_default** | **bool** |  | 

## Example

```python
from taikunpycore.models.cloud_credentials_for_organization_entity import CloudCredentialsForOrganizationEntity

# TODO update the JSON string below
json = "{}"
# create an instance of CloudCredentialsForOrganizationEntity from a JSON string
cloud_credentials_for_organization_entity_instance = CloudCredentialsForOrganizationEntity.from_json(json)
# print the JSON string representation of the object
print(CloudCredentialsForOrganizationEntity.to_json())

# convert the object into a dict
cloud_credentials_for_organization_entity_dict = cloud_credentials_for_organization_entity_instance.to_dict()
# create an instance of CloudCredentialsForOrganizationEntity from a dict
cloud_credentials_for_organization_entity_from_dict = CloudCredentialsForOrganizationEntity.from_dict(cloud_credentials_for_organization_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


