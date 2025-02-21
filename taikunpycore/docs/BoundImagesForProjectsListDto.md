# BoundImagesForProjectsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**project_id** | **int** |  | 
**project_name** | **str** |  | 
**size** | **float** |  | 
**image_id** | **str** |  | 
**cloud_id** | **int** |  | 
**is_windows** | **bool** |  | 
**cloud_type** | [**CloudType**](CloudType.md) |  | 

## Example

```python
from taikunpycore.models.bound_images_for_projects_list_dto import BoundImagesForProjectsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of BoundImagesForProjectsListDto from a JSON string
bound_images_for_projects_list_dto_instance = BoundImagesForProjectsListDto.from_json(json)
# print the JSON string representation of the object
print(BoundImagesForProjectsListDto.to_json())

# convert the object into a dict
bound_images_for_projects_list_dto_dict = bound_images_for_projects_list_dto_instance.to_dict()
# create an instance of BoundImagesForProjectsListDto from a dict
bound_images_for_projects_list_dto_from_dict = BoundImagesForProjectsListDto.from_dict(bound_images_for_projects_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


