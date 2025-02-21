# BoundFlavorsForProjectsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BoundFlavorsForProjectsListDto]**](BoundFlavorsForProjectsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.bound_flavors_for_projects_list import BoundFlavorsForProjectsList

# TODO update the JSON string below
json = "{}"
# create an instance of BoundFlavorsForProjectsList from a JSON string
bound_flavors_for_projects_list_instance = BoundFlavorsForProjectsList.from_json(json)
# print the JSON string representation of the object
print(BoundFlavorsForProjectsList.to_json())

# convert the object into a dict
bound_flavors_for_projects_list_dict = bound_flavors_for_projects_list_instance.to_dict()
# create an instance of BoundFlavorsForProjectsList from a dict
bound_flavors_for_projects_list_from_dict = BoundFlavorsForProjectsList.from_dict(bound_flavors_for_projects_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


