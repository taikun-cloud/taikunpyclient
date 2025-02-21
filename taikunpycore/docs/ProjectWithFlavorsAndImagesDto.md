# ProjectWithFlavorsAndImagesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**flavors** | **List[str]** |  | 
**images** | **List[str]** |  | 
**image_names** | **List[str]** |  | 
**is_ready** | **bool** |  | 

## Example

```python
from taikunpycore.models.project_with_flavors_and_images_dto import ProjectWithFlavorsAndImagesDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectWithFlavorsAndImagesDto from a JSON string
project_with_flavors_and_images_dto_instance = ProjectWithFlavorsAndImagesDto.from_json(json)
# print the JSON string representation of the object
print(ProjectWithFlavorsAndImagesDto.to_json())

# convert the object into a dict
project_with_flavors_and_images_dto_dict = project_with_flavors_and_images_dto_instance.to_dict()
# create an instance of ProjectWithFlavorsAndImagesDto from a dict
project_with_flavors_and_images_dto_from_dict = ProjectWithFlavorsAndImagesDto.from_dict(project_with_flavors_and_images_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


