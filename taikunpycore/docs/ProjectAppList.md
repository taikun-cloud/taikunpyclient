# ProjectAppList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InstanceAppListDto]**](InstanceAppListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.project_app_list import ProjectAppList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectAppList from a JSON string
project_app_list_instance = ProjectAppList.from_json(json)
# print the JSON string representation of the object
print(ProjectAppList.to_json())

# convert the object into a dict
project_app_list_dict = project_app_list_instance.to_dict()
# create an instance of ProjectAppList from a dict
project_app_list_from_dict = ProjectAppList.from_dict(project_app_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


