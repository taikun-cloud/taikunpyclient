# ConfigMaps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ConfigMapDto]**](ConfigMapDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.config_maps import ConfigMaps

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigMaps from a JSON string
config_maps_instance = ConfigMaps.from_json(json)
# print the JSON string representation of the object
print(ConfigMaps.to_json())

# convert the object into a dict
config_maps_dict = config_maps_instance.to_dict()
# create an instance of ConfigMaps from a dict
config_maps_from_dict = ConfigMaps.from_dict(config_maps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


