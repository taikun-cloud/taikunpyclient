# CommonSearchKubernetesResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**project_name** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**organization_name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.common_search_kubernetes_response_data import CommonSearchKubernetesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSearchKubernetesResponseData from a JSON string
common_search_kubernetes_response_data_instance = CommonSearchKubernetesResponseData.from_json(json)
# print the JSON string representation of the object
print(CommonSearchKubernetesResponseData.to_json())

# convert the object into a dict
common_search_kubernetes_response_data_dict = common_search_kubernetes_response_data_instance.to_dict()
# create an instance of CommonSearchKubernetesResponseData from a dict
common_search_kubernetes_response_data_from_dict = CommonSearchKubernetesResponseData.from_dict(common_search_kubernetes_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


