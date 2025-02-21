# SpotVmOperationCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.spot_vm_operation_command import SpotVmOperationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SpotVmOperationCommand from a JSON string
spot_vm_operation_command_instance = SpotVmOperationCommand.from_json(json)
# print the JSON string representation of the object
print(SpotVmOperationCommand.to_json())

# convert the object into a dict
spot_vm_operation_command_dict = spot_vm_operation_command_instance.to_dict()
# create an instance of SpotVmOperationCommand from a dict
spot_vm_operation_command_from_dict = SpotVmOperationCommand.from_dict(spot_vm_operation_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


