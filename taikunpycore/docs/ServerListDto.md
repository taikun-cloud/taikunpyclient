# ServerListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**project_name** | **str** |  | 
**organization_name** | **str** |  | 
**organization_id** | **int** |  | 
**project_id** | **int** |  | 
**ip_address** | **str** |  | 
**disk_size** | **float** |  | 
**kubernetes_health** | **str** |  | 
**cpu** | **int** |  | 
**ram** | **float** |  | 
**role** | [**CloudRole**](CloudRole.md) |  | 
**status** | **str** |  | 
**created_at** | **str** |  | 
**cloud_type** | [**CloudType**](CloudType.md) |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**spot_price** | **float** |  | 
**spot_instance** | **bool** |  | 
**shut_off** | **bool** |  | 
**autoscaling_group** | **str** |  | 
**provider_id** | **str** |  | 
**instance_id** | **str** |  | 
**aws_host_name** | **str** |  | 
**availability_zone** | **str** |  | 
**hypervisor** | **str** |  | 
**hypervisor_id** | **str** |  | 
**proxmox_role** | [**ProxmoxRole**](ProxmoxRole.md) |  | 
**proxmox_extra_disk_size** | **int** |  | 
**action_buttons** | [**ServerActionButtonVisibilityDto**](ServerActionButtonVisibilityDto.md) |  | [optional] 
**kubernetes_node_labels** | [**List[KubernetesNodeLabelsDto]**](KubernetesNodeLabelsDto.md) |  | 
**replica_count** | **int** |  | 
**wasm_enabled** | **bool** |  | 
**flavor** | **str** |  | 

## Example

```python
from taikunpycore.models.server_list_dto import ServerListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerListDto from a JSON string
server_list_dto_instance = ServerListDto.from_json(json)
# print the JSON string representation of the object
print(ServerListDto.to_json())

# convert the object into a dict
server_list_dto_dict = server_list_dto_instance.to_dict()
# create an instance of ServerListDto from a dict
server_list_dto_from_dict = ServerListDto.from_dict(server_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


