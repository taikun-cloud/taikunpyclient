# PatchKubernetesResourceCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**yaml** | **str** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.patch_kubernetes_resource_command import PatchKubernetesResourceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PatchKubernetesResourceCommand from a JSON string
patch_kubernetes_resource_command_instance = PatchKubernetesResourceCommand.from_json(json)
# print the JSON string representation of the object
print(PatchKubernetesResourceCommand.to_json())

# convert the object into a dict
patch_kubernetes_resource_command_dict = patch_kubernetes_resource_command_instance.to_dict()
# create an instance of PatchKubernetesResourceCommand from a dict
patch_kubernetes_resource_command_from_dict = PatchKubernetesResourceCommand.from_dict(patch_kubernetes_resource_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


