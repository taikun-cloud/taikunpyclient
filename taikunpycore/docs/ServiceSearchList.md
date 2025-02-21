# ServiceSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchKubernetesResponseData]**](CommonSearchKubernetesResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.service_search_list import ServiceSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSearchList from a JSON string
service_search_list_instance = ServiceSearchList.from_json(json)
# print the JSON string representation of the object
print(ServiceSearchList.to_json())

# convert the object into a dict
service_search_list_dict = service_search_list_instance.to_dict()
# create an instance of ServiceSearchList from a dict
service_search_list_from_dict = ServiceSearchList.from_dict(service_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


