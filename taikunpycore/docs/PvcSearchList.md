# PvcSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchKubernetesResponseData]**](CommonSearchKubernetesResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.pvc_search_list import PvcSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of PvcSearchList from a JSON string
pvc_search_list_instance = PvcSearchList.from_json(json)
# print the JSON string representation of the object
print(PvcSearchList.to_json())

# convert the object into a dict
pvc_search_list_dict = pvc_search_list_instance.to_dict()
# create an instance of PvcSearchList from a dict
pvc_search_list_from_dict = PvcSearchList.from_dict(pvc_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


