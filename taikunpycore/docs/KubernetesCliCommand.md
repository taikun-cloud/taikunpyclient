# KubernetesCliCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**kube_config_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_cli_command import KubernetesCliCommand

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesCliCommand from a JSON string
kubernetes_cli_command_instance = KubernetesCliCommand.from_json(json)
# print the JSON string representation of the object
print(KubernetesCliCommand.to_json())

# convert the object into a dict
kubernetes_cli_command_dict = kubernetes_cli_command_instance.to_dict()
# create an instance of KubernetesCliCommand from a dict
kubernetes_cli_command_from_dict = KubernetesCliCommand.from_dict(kubernetes_cli_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


