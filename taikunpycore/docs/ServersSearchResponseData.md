# ServersSearchResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**project_name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.servers_search_response_data import ServersSearchResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ServersSearchResponseData from a JSON string
servers_search_response_data_instance = ServersSearchResponseData.from_json(json)
# print the JSON string representation of the object
print(ServersSearchResponseData.to_json())

# convert the object into a dict
servers_search_response_data_dict = servers_search_response_data_instance.to_dict()
# create an instance of ServersSearchResponseData from a dict
servers_search_response_data_from_dict = ServersSearchResponseData.from_dict(servers_search_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


