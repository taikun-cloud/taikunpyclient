# EndpointElements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**controller** | **str** |  | 
**description** | **str** |  | 
**method** | **str** |  | 
**path** | **str** |  | 

## Example

```python
from taikunpycore.models.endpoint_elements import EndpointElements

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointElements from a JSON string
endpoint_elements_instance = EndpointElements.from_json(json)
# print the JSON string representation of the object
print(EndpointElements.to_json())

# convert the object into a dict
endpoint_elements_dict = endpoint_elements_instance.to_dict()
# create an instance of EndpointElements from a dict
endpoint_elements_from_dict = EndpointElements.from_dict(endpoint_elements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


