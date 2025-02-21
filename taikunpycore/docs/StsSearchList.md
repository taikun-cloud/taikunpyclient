# StsSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchKubernetesResponseData]**](CommonSearchKubernetesResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.sts_search_list import StsSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of StsSearchList from a JSON string
sts_search_list_instance = StsSearchList.from_json(json)
# print the JSON string representation of the object
print(StsSearchList.to_json())

# convert the object into a dict
sts_search_list_dict = sts_search_list_instance.to_dict()
# create an instance of StsSearchList from a dict
sts_search_list_from_dict = StsSearchList.from_dict(sts_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


