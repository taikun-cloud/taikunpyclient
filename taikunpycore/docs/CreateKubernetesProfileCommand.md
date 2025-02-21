# CreateKubernetesProfileCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**octavia_enabled** | **bool** |  | [optional] 
**expose_node_port_on_bastion** | **bool** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**taikun_lb_enabled** | **bool** |  | [optional] 
**allow_scheduling_on_master** | **bool** |  | [optional] 
**unique_cluster_name** | **bool** |  | [optional] 
**proxmox_storage** | [**ProxmoxStorage**](ProxmoxStorage.md) |  | [optional] 
**nvidia_gpu_operator_enabled** | **bool** |  | [optional] 
**wasm_enabled** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.create_kubernetes_profile_command import CreateKubernetesProfileCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKubernetesProfileCommand from a JSON string
create_kubernetes_profile_command_instance = CreateKubernetesProfileCommand.from_json(json)
# print the JSON string representation of the object
print(CreateKubernetesProfileCommand.to_json())

# convert the object into a dict
create_kubernetes_profile_command_dict = create_kubernetes_profile_command_instance.to_dict()
# create an instance of CreateKubernetesProfileCommand from a dict
create_kubernetes_profile_command_from_dict = CreateKubernetesProfileCommand.from_dict(create_kubernetes_profile_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


