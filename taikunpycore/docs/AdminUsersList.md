# AdminUsersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminUsersResponseData]**](AdminUsersResponseData.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.admin_users_list import AdminUsersList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUsersList from a JSON string
admin_users_list_instance = AdminUsersList.from_json(json)
# print the JSON string representation of the object
print(AdminUsersList.to_json())

# convert the object into a dict
admin_users_list_dict = admin_users_list_instance.to_dict()
# create an instance of AdminUsersList from a dict
admin_users_list_from_dict = AdminUsersList.from_dict(admin_users_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


