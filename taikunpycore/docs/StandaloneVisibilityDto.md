# StandaloneVisibilityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**show_status** | **bool** |  | 
**show_console** | **bool** |  | 
**shelve** | **bool** |  | 
**unshelve** | **bool** |  | 
**start** | **bool** |  | 
**stop** | **bool** |  | 
**reboot** | **bool** |  | 

## Example

```python
from taikunpycore.models.standalone_visibility_dto import StandaloneVisibilityDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandaloneVisibilityDto from a JSON string
standalone_visibility_dto_instance = StandaloneVisibilityDto.from_json(json)
# print the JSON string representation of the object
print(StandaloneVisibilityDto.to_json())

# convert the object into a dict
standalone_visibility_dto_dict = standalone_visibility_dto_instance.to_dict()
# create an instance of StandaloneVisibilityDto from a dict
standalone_visibility_dto_from_dict = StandaloneVisibilityDto.from_dict(standalone_visibility_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


