# NodeSearchResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**project_name** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**organization_name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.node_search_response_data import NodeSearchResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of NodeSearchResponseData from a JSON string
node_search_response_data_instance = NodeSearchResponseData.from_json(json)
# print the JSON string representation of the object
print(NodeSearchResponseData.to_json())

# convert the object into a dict
node_search_response_data_dict = node_search_response_data_instance.to_dict()
# create an instance of NodeSearchResponseData from a dict
node_search_response_data_from_dict = NodeSearchResponseData.from_dict(node_search_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


