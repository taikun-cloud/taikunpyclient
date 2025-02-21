# InfraOrganizationsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**billing_start_date** | **datetime** |  | [optional] 
**yearly** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.infra_organizations_list_dto import InfraOrganizationsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of InfraOrganizationsListDto from a JSON string
infra_organizations_list_dto_instance = InfraOrganizationsListDto.from_json(json)
# print the JSON string representation of the object
print(InfraOrganizationsListDto.to_json())

# convert the object into a dict
infra_organizations_list_dto_dict = infra_organizations_list_dto_instance.to_dict()
# create an instance of InfraOrganizationsListDto from a dict
infra_organizations_list_dto_from_dict = InfraOrganizationsListDto.from_dict(infra_organizations_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


