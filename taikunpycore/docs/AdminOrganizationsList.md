# AdminOrganizationsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminOrganizationsListDto]**](AdminOrganizationsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.admin_organizations_list import AdminOrganizationsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminOrganizationsList from a JSON string
admin_organizations_list_instance = AdminOrganizationsList.from_json(json)
# print the JSON string representation of the object
print(AdminOrganizationsList.to_json())

# convert the object into a dict
admin_organizations_list_dict = admin_organizations_list_instance.to_dict()
# create an instance of AdminOrganizationsList from a dict
admin_organizations_list_from_dict = AdminOrganizationsList.from_dict(admin_organizations_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


