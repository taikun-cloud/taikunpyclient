# AvailableEndpointsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EndpointElements]**](EndpointElements.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.available_endpoints_list import AvailableEndpointsList

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableEndpointsList from a JSON string
available_endpoints_list_instance = AvailableEndpointsList.from_json(json)
# print the JSON string representation of the object
print(AvailableEndpointsList.to_json())

# convert the object into a dict
available_endpoints_list_dict = available_endpoints_list_instance.to_dict()
# create an instance of AvailableEndpointsList from a dict
available_endpoints_list_from_dict = AvailableEndpointsList.from_dict(available_endpoints_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


