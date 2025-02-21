# PodsSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchKubernetesResponseData]**](CommonSearchKubernetesResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.pods_search_list import PodsSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of PodsSearchList from a JSON string
pods_search_list_instance = PodsSearchList.from_json(json)
# print the JSON string representation of the object
print(PodsSearchList.to_json())

# convert the object into a dict
pods_search_list_dict = pods_search_list_instance.to_dict()
# create an instance of PodsSearchList from a dict
pods_search_list_from_dict = PodsSearchList.from_dict(pods_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


