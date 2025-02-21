# KubernetesProfilesListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**cni** | [**CNI**](CNI.md) |  | 
**octavia_enabled** | **bool** |  | 
**expose_node_port_on_bastion** | **bool** |  | 
**is_locked** | **bool** |  | 
**taikun_lb_enabled** | **bool** |  | 
**allow_scheduling_on_master** | **bool** |  | 
**unique_cluster_name** | **bool** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**created_by** | **str** |  | 
**created_at** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**proxmox_storage** | [**ProxmoxStorage**](ProxmoxStorage.md) |  | 
**nvidia_gpu_operator_enabled** | **bool** |  | 
**wasm_enabled** | **bool** |  | 

## Example

```python
from taikunpycore.models.kubernetes_profiles_list_dto import KubernetesProfilesListDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesProfilesListDto from a JSON string
kubernetes_profiles_list_dto_instance = KubernetesProfilesListDto.from_json(json)
# print the JSON string representation of the object
print(KubernetesProfilesListDto.to_json())

# convert the object into a dict
kubernetes_profiles_list_dto_dict = kubernetes_profiles_list_dto_instance.to_dict()
# create an instance of KubernetesProfilesListDto from a dict
kubernetes_profiles_list_dto_from_dict = KubernetesProfilesListDto.from_dict(kubernetes_profiles_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


