# ProjectGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProjectGroupDetailsListDto]**](ProjectGroupDetailsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.project_group_list import ProjectGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectGroupList from a JSON string
project_group_list_instance = ProjectGroupList.from_json(json)
# print the JSON string representation of the object
print(ProjectGroupList.to_json())

# convert the object into a dict
project_group_list_dict = project_group_list_instance.to_dict()
# create an instance of ProjectGroupList from a dict
project_group_list_from_dict = ProjectGroupList.from_dict(project_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


