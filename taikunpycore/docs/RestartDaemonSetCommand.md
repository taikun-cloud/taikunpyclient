# RestartDaemonSetCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.restart_daemon_set_command import RestartDaemonSetCommand

# TODO update the JSON string below
json = "{}"
# create an instance of RestartDaemonSetCommand from a JSON string
restart_daemon_set_command_instance = RestartDaemonSetCommand.from_json(json)
# print the JSON string representation of the object
print(RestartDaemonSetCommand.to_json())

# convert the object into a dict
restart_daemon_set_command_dict = restart_daemon_set_command_instance.to_dict()
# create an instance of RestartDaemonSetCommand from a dict
restart_daemon_set_command_from_dict = RestartDaemonSetCommand.from_dict(restart_daemon_set_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


