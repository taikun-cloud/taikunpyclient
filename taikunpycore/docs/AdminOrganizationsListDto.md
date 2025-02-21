# AdminOrganizationsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**customer_id** | **str** |  | 
**partner_name** | **str** |  | 
**partner_logo** | **str** |  | 

## Example

```python
from taikunpycore.models.admin_organizations_list_dto import AdminOrganizationsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdminOrganizationsListDto from a JSON string
admin_organizations_list_dto_instance = AdminOrganizationsListDto.from_json(json)
# print the JSON string representation of the object
print(AdminOrganizationsListDto.to_json())

# convert the object into a dict
admin_organizations_list_dto_dict = admin_organizations_list_dto_instance.to_dict()
# create an instance of AdminOrganizationsListDto from a dict
admin_organizations_list_dto_from_dict = AdminOrganizationsListDto.from_dict(admin_organizations_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


