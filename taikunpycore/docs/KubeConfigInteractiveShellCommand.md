# KubeConfigInteractiveShellCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kube_config_id** | **int** |  | [optional] 
**token** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.kube_config_interactive_shell_command import KubeConfigInteractiveShellCommand

# TODO update the JSON string below
json = "{}"
# create an instance of KubeConfigInteractiveShellCommand from a JSON string
kube_config_interactive_shell_command_instance = KubeConfigInteractiveShellCommand.from_json(json)
# print the JSON string representation of the object
print(KubeConfigInteractiveShellCommand.to_json())

# convert the object into a dict
kube_config_interactive_shell_command_dict = kube_config_interactive_shell_command_instance.to_dict()
# create an instance of KubeConfigInteractiveShellCommand from a dict
kube_config_interactive_shell_command_from_dict = KubeConfigInteractiveShellCommand.from_dict(kube_config_interactive_shell_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


