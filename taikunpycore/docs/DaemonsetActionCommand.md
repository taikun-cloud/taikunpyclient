# DaemonsetActionCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | 
**action** | [**EDaemonSetAction**](EDaemonSetAction.md) |  | 

## Example

```python
from taikunpycore.models.daemonset_action_command import DaemonsetActionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DaemonsetActionCommand from a JSON string
daemonset_action_command_instance = DaemonsetActionCommand.from_json(json)
# print the JSON string representation of the object
print(DaemonsetActionCommand.to_json())

# convert the object into a dict
daemonset_action_command_dict = daemonset_action_command_instance.to_dict()
# create an instance of DaemonsetActionCommand from a dict
daemonset_action_command_from_dict = DaemonsetActionCommand.from_dict(daemonset_action_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


