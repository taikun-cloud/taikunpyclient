# InteractiveShellSendCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**token** | **str** |  | [optional] 
**instance_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.interactive_shell_send_command import InteractiveShellSendCommand

# TODO update the JSON string below
json = "{}"
# create an instance of InteractiveShellSendCommand from a JSON string
interactive_shell_send_command_instance = InteractiveShellSendCommand.from_json(json)
# print the JSON string representation of the object
print(InteractiveShellSendCommand.to_json())

# convert the object into a dict
interactive_shell_send_command_dict = interactive_shell_send_command_instance.to_dict()
# create an instance of InteractiveShellSendCommand from a dict
interactive_shell_send_command_from_dict = InteractiveShellSendCommand.from_dict(interactive_shell_send_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


