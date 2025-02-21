# UpdateGenericKubernetesCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_generic_kubernetes_command import UpdateGenericKubernetesCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGenericKubernetesCommand from a JSON string
update_generic_kubernetes_command_instance = UpdateGenericKubernetesCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateGenericKubernetesCommand.to_json())

# convert the object into a dict
update_generic_kubernetes_command_dict = update_generic_kubernetes_command_instance.to_dict()
# create an instance of UpdateGenericKubernetesCommand from a dict
update_generic_kubernetes_command_from_dict = UpdateGenericKubernetesCommand.from_dict(update_generic_kubernetes_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


