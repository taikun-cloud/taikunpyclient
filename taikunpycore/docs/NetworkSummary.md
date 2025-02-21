# NetworkSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.network_summary import NetworkSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkSummary from a JSON string
network_summary_instance = NetworkSummary.from_json(json)
# print the JSON string representation of the object
print(NetworkSummary.to_json())

# convert the object into a dict
network_summary_dict = network_summary_instance.to_dict()
# create an instance of NetworkSummary from a dict
network_summary_from_dict = NetworkSummary.from_dict(network_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


