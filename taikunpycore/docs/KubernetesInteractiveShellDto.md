# KubernetesInteractiveShellDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kube_config** | **str** |  | [optional] 
**pod_name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.kubernetes_interactive_shell_dto import KubernetesInteractiveShellDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesInteractiveShellDto from a JSON string
kubernetes_interactive_shell_dto_instance = KubernetesInteractiveShellDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesInteractiveShellDto.to_json())

# convert the object into a dict
kubernetes_interactive_shell_dto_dict = kubernetes_interactive_shell_dto_instance.to_dict()
# create an instance of KubernetesInteractiveShellDto from a dict
kubernetes_interactive_shell_dto_from_dict = KubernetesInteractiveShellDto.from_dict(kubernetes_interactive_shell_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


