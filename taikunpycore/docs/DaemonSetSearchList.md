# DaemonSetSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchKubernetesResponseData]**](CommonSearchKubernetesResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.daemon_set_search_list import DaemonSetSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of DaemonSetSearchList from a JSON string
daemon_set_search_list_instance = DaemonSetSearchList.from_json(json)
# print the JSON string representation of the object
print(DaemonSetSearchList.to_json())

# convert the object into a dict
daemon_set_search_list_dict = daemon_set_search_list_instance.to_dict()
# create an instance of DaemonSetSearchList from a dict
daemon_set_search_list_from_dict = DaemonSetSearchList.from_dict(daemon_set_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


