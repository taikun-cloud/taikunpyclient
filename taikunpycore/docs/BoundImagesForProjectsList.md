# BoundImagesForProjectsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BoundImagesForProjectsListDto]**](BoundImagesForProjectsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.bound_images_for_projects_list import BoundImagesForProjectsList

# TODO update the JSON string below
json = "{}"
# create an instance of BoundImagesForProjectsList from a JSON string
bound_images_for_projects_list_instance = BoundImagesForProjectsList.from_json(json)
# print the JSON string representation of the object
print(BoundImagesForProjectsList.to_json())

# convert the object into a dict
bound_images_for_projects_list_dict = bound_images_for_projects_list_instance.to_dict()
# create an instance of BoundImagesForProjectsList from a dict
bound_images_for_projects_list_from_dict = BoundImagesForProjectsList.from_dict(bound_images_for_projects_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


