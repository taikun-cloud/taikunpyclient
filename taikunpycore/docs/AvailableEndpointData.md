# AvailableEndpointData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**controller** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.available_endpoint_data import AvailableEndpointData

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableEndpointData from a JSON string
available_endpoint_data_instance = AvailableEndpointData.from_json(json)
# print the JSON string representation of the object
print(AvailableEndpointData.to_json())

# convert the object into a dict
available_endpoint_data_dict = available_endpoint_data_instance.to_dict()
# create an instance of AvailableEndpointData from a dict
available_endpoint_data_from_dict = AvailableEndpointData.from_dict(available_endpoint_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


