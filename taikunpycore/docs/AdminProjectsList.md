# AdminProjectsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AdminProjectsResponseData]**](AdminProjectsResponseData.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.admin_projects_list import AdminProjectsList

# TODO update the JSON string below
json = "{}"
# create an instance of AdminProjectsList from a JSON string
admin_projects_list_instance = AdminProjectsList.from_json(json)
# print the JSON string representation of the object
print(AdminProjectsList.to_json())

# convert the object into a dict
admin_projects_list_dict = admin_projects_list_instance.to_dict()
# create an instance of AdminProjectsList from a dict
admin_projects_list_from_dict = AdminProjectsList.from_dict(admin_projects_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


