# OrganizationDropdownDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**is_infra** | **bool** |  | [optional] 
**discount_rate** | **float** |  | [optional] 

## Example

```python
from taikunpycore.models.organization_dropdown_dto import OrganizationDropdownDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationDropdownDto from a JSON string
organization_dropdown_dto_instance = OrganizationDropdownDto.from_json(json)
# print the JSON string representation of the object
print(OrganizationDropdownDto.to_json())

# convert the object into a dict
organization_dropdown_dto_dict = organization_dropdown_dto_instance.to_dict()
# create an instance of OrganizationDropdownDto from a dict
organization_dropdown_dto_from_dict = OrganizationDropdownDto.from_dict(organization_dropdown_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


