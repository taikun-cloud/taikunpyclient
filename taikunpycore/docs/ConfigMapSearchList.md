# ConfigMapSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchKubernetesResponseData]**](CommonSearchKubernetesResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.config_map_search_list import ConfigMapSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigMapSearchList from a JSON string
config_map_search_list_instance = ConfigMapSearchList.from_json(json)
# print the JSON string representation of the object
print(ConfigMapSearchList.to_json())

# convert the object into a dict
config_map_search_list_dict = config_map_search_list_instance.to_dict()
# create an instance of ConfigMapSearchList from a dict
config_map_search_list_from_dict = ConfigMapSearchList.from_dict(config_map_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


