# ProjectsSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchResponseData]**](CommonSearchResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.projects_search_list import ProjectsSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsSearchList from a JSON string
projects_search_list_instance = ProjectsSearchList.from_json(json)
# print the JSON string representation of the object
print(ProjectsSearchList.to_json())

# convert the object into a dict
projects_search_list_dict = projects_search_list_instance.to_dict()
# create an instance of ProjectsSearchList from a dict
projects_search_list_from_dict = ProjectsSearchList.from_dict(projects_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


