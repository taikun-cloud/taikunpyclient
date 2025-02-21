# ConfigMapDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | 
**namespace** | **str** |  | 
**age** | **str** |  | 

## Example

```python
from taikunpycore.models.config_map_dto import ConfigMapDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigMapDto from a JSON string
config_map_dto_instance = ConfigMapDto.from_json(json)
# print the JSON string representation of the object
print(ConfigMapDto.to_json())

# convert the object into a dict
config_map_dto_dict = config_map_dto_instance.to_dict()
# create an instance of ConfigMapDto from a dict
config_map_dto_from_dict = ConfigMapDto.from_dict(config_map_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


