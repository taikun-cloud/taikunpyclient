# DatacenterListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**datacenter_name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.datacenter_list_command import DatacenterListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DatacenterListCommand from a JSON string
datacenter_list_command_instance = DatacenterListCommand.from_json(json)
# print the JSON string representation of the object
print(DatacenterListCommand.to_json())

# convert the object into a dict
datacenter_list_command_dict = datacenter_list_command_instance.to_dict()
# create an instance of DatacenterListCommand from a dict
datacenter_list_command_from_dict = DatacenterListCommand.from_dict(datacenter_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


