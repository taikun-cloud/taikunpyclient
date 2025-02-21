# ServerForCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**role** | [**CloudRole**](CloudRole.md) |  | [optional] 
**project_id** | **int** |  | [optional] 
**disk_size** | **float** |  | [optional] 
**flavor** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**spot_price** | **float** |  | [optional] 
**spot_instance** | **bool** |  | [optional] 
**wasm_enabled** | **bool** |  | [optional] 
**autoscaling_group** | **str** |  | [optional] 
**availability_zone** | **str** |  | [optional] 
**proxmox_extra_disk_size** | **int** |  | [optional] 
**proxmox_role** | [**ProxmoxRole**](ProxmoxRole.md) |  | [optional] 
**hypervisor** | **str** |  | [optional] 
**kubernetes_node_labels** | [**List[KubernetesNodeLabelsDto]**](KubernetesNodeLabelsDto.md) |  | [optional] 
**replica_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.server_for_create_dto import ServerForCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerForCreateDto from a JSON string
server_for_create_dto_instance = ServerForCreateDto.from_json(json)
# print the JSON string representation of the object
print(ServerForCreateDto.to_json())

# convert the object into a dict
server_for_create_dto_dict = server_for_create_dto_instance.to_dict()
# create an instance of ServerForCreateDto from a dict
server_for_create_dto_from_dict = ServerForCreateDto.from_dict(server_for_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


