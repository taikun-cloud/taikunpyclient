# StandAloneVmIpManagementCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.stand_alone_vm_ip_management_command import StandAloneVmIpManagementCommand

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneVmIpManagementCommand from a JSON string
stand_alone_vm_ip_management_command_instance = StandAloneVmIpManagementCommand.from_json(json)
# print the JSON string representation of the object
print(StandAloneVmIpManagementCommand.to_json())

# convert the object into a dict
stand_alone_vm_ip_management_command_dict = stand_alone_vm_ip_management_command_instance.to_dict()
# create an instance of StandAloneVmIpManagementCommand from a dict
stand_alone_vm_ip_management_command_from_dict = StandAloneVmIpManagementCommand.from_dict(stand_alone_vm_ip_management_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


