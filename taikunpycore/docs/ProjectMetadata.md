# ProjectMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**vcs_sub_path** | **str** |  | [optional] 
**providers** | [**List[Provider]**](Provider.md) |  | [optional] 

## Example

```python
from taikunpycore.models.project_metadata import ProjectMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectMetadata from a JSON string
project_metadata_instance = ProjectMetadata.from_json(json)
# print the JSON string representation of the object
print(ProjectMetadata.to_json())

# convert the object into a dict
project_metadata_dict = project_metadata_instance.to_dict()
# create an instance of ProjectMetadata from a dict
project_metadata_from_dict = ProjectMetadata.from_dict(project_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


