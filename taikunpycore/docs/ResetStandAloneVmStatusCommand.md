# ResetStandAloneVmStatusCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**vm_ids** | **List[int]** |  | [optional] 
**status** | [**StandAloneVmStatus**](StandAloneVmStatus.md) |  | [optional] 

## Example

```python
from taikunpycore.models.reset_stand_alone_vm_status_command import ResetStandAloneVmStatusCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ResetStandAloneVmStatusCommand from a JSON string
reset_stand_alone_vm_status_command_instance = ResetStandAloneVmStatusCommand.from_json(json)
# print the JSON string representation of the object
print(ResetStandAloneVmStatusCommand.to_json())

# convert the object into a dict
reset_stand_alone_vm_status_command_dict = reset_stand_alone_vm_status_command_instance.to_dict()
# create an instance of ResetStandAloneVmStatusCommand from a dict
reset_stand_alone_vm_status_command_from_dict = ResetStandAloneVmStatusCommand.from_dict(reset_stand_alone_vm_status_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


