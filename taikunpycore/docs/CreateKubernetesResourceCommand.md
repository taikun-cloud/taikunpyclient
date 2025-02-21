# CreateKubernetesResourceCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**yaml** | **str** |  | 

## Example

```python
from taikunpycore.models.create_kubernetes_resource_command import CreateKubernetesResourceCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKubernetesResourceCommand from a JSON string
create_kubernetes_resource_command_instance = CreateKubernetesResourceCommand.from_json(json)
# print the JSON string representation of the object
print(CreateKubernetesResourceCommand.to_json())

# convert the object into a dict
create_kubernetes_resource_command_dict = create_kubernetes_resource_command_instance.to_dict()
# create an instance of CreateKubernetesResourceCommand from a dict
create_kubernetes_resource_command_from_dict = CreateKubernetesResourceCommand.from_dict(create_kubernetes_resource_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


