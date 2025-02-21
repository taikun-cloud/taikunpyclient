# DeleteKubernetesResourceCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**kind** | [**EKubernetesResource**](EKubernetesResource.md) |  | 
**data** | [**List[KubernetesActionRequest]**](KubernetesActionRequest.md) |  | 

## Example

```python
from taikunpycore.models.delete_kubernetes_resource_command import DeleteKubernetesResourceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteKubernetesResourceCommand from a JSON string
delete_kubernetes_resource_command_instance = DeleteKubernetesResourceCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteKubernetesResourceCommand.to_json())

# convert the object into a dict
delete_kubernetes_resource_command_dict = delete_kubernetes_resource_command_instance.to_dict()
# create an instance of DeleteKubernetesResourceCommand from a dict
delete_kubernetes_resource_command_from_dict = DeleteKubernetesResourceCommand.from_dict(delete_kubernetes_resource_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


