# IngressSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchKubernetesResponseData]**](CommonSearchKubernetesResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.ingress_search_list import IngressSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of IngressSearchList from a JSON string
ingress_search_list_instance = IngressSearchList.from_json(json)
# print the JSON string representation of the object
print(IngressSearchList.to_json())

# convert the object into a dict
ingress_search_list_dict = ingress_search_list_instance.to_dict()
# create an instance of IngressSearchList from a dict
ingress_search_list_from_dict = IngressSearchList.from_dict(ingress_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


