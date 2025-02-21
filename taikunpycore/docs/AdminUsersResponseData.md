# AdminUsersResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**role** | [**UserRole**](UserRole.md) |  | 
**organization_name** | **str** |  | 
**owner** | **bool** |  | 
**csm** | **bool** |  | 

## Example

```python
from taikunpycore.models.admin_users_response_data import AdminUsersResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUsersResponseData from a JSON string
admin_users_response_data_instance = AdminUsersResponseData.from_json(json)
# print the JSON string representation of the object
print(AdminUsersResponseData.to_json())

# convert the object into a dict
admin_users_response_data_dict = admin_users_response_data_instance.to_dict()
# create an instance of AdminUsersResponseData from a dict
admin_users_response_data_from_dict = AdminUsersResponseData.from_dict(admin_users_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


