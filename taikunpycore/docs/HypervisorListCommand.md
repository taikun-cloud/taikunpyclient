# HypervisorListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**token_secret** | **str** |  | [optional] 
**cloud_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.hypervisor_list_command import HypervisorListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of HypervisorListCommand from a JSON string
hypervisor_list_command_instance = HypervisorListCommand.from_json(json)
# print the JSON string representation of the object
print(HypervisorListCommand.to_json())

# convert the object into a dict
hypervisor_list_command_dict = hypervisor_list_command_instance.to_dict()
# create an instance of HypervisorListCommand from a dict
hypervisor_list_command_from_dict = HypervisorListCommand.from_dict(hypervisor_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


