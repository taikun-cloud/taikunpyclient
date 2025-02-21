# ProjectDetailsForServersDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts_count** | **int** |  | 
**worker** | **int** |  | 
**bastion** | **int** |  | 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | 
**name** | **str** |  | 
**access_ip** | **str** |  | 
**id** | **int** |  | 
**master_ready** | **int** |  | 
**cloud_type** | [**CloudType**](CloudType.md) |  | 
**cloud_name** | **str** |  | 
**cloud_id** | **int** |  | 
**quota_id** | **int** |  | 
**organization_name** | **str** |  | 
**organization_id** | **int** |  | 
**kubernetes_version** | **str** |  | 
**is_backup_enabled** | **bool** |  | 
**ai_enabled** | **bool** |  | 
**is_locked** | **bool** |  | 
**is_auto_upgrade** | **bool** |  | 
**is_monitoring_enabled** | **bool** |  | 
**is_opa_enabled** | **bool** |  | 
**has_kube_config_file** | **bool** |  | 
**has_selected_flavors** | **bool** |  | 
**is_maintenance_mode_enabled** | **bool** |  | 
**is_project_maintenance_mode_enabled** | **bool** |  | 
**is_deprecated** | **bool** |  | 
**cpu_limit** | **int** |  | 
**ram_limit** | **int** |  | 
**disk_size_limit** | **int** |  | 
**used_cpu** | **int** |  | 
**used_ram** | **int** |  | 
**used_disk_size** | **int** |  | 
**vm_cpu_limit** | **int** |  | 
**vm_ram_limit** | **int** |  | 
**vm_volume_size_limit** | **int** |  | 
**vm_used_cpu** | **int** |  | 
**vm_used_ram** | **int** |  | 
**vm_used_volume_size** | **int** |  | 
**access_profile_name** | **str** |  | 
**access_profile_id** | **int** |  | 
**kubernetes_profile_name** | **str** |  | 
**kubernetes_profile_id** | **int** |  | 
**alerting_profile_name** | **str** |  | 
**health** | [**ProjectHealth**](ProjectHealth.md) |  | 
**alerting_profile_id** | **int** |  | 
**s3_credential_id** | **int** |  | 
**ai_credential_id** | **int** |  | 
**expired_at** | **str** |  | 
**certification_expired_at** | **str** |  | 
**opa_profile_id** | **int** |  | 
**opa_profile_name** | **str** |  | 
**allow_full_spot_kubernetes** | **bool** |  | 
**allow_spot_workers** | **bool** |  | 
**allow_spot_vms** | **bool** |  | 
**total_hourly_cost** | **float** |  | 
**autoscaling_group_name** | **str** |  | 
**min_size** | **int** |  | 
**max_size** | **int** |  | 
**disk_size** | **float** |  | 
**flavor** | **str** |  | 
**spot_enabled** | **bool** |  | 
**is_autoscaling_enabled** | **bool** |  | 
**is_autoscaling_spot_enabled** | **bool** |  | 
**has_nfs_server** | **bool** |  | 
**wasm_enabled** | **bool** |  | 
**availability_zones** | **List[str]** |  | 
**hypervisors** | **List[str]** |  | 
**proxmox_storage** | [**ProxmoxStorage**](ProxmoxStorage.md) |  | 
**is_drs_enabled** | **bool** |  | 
**max_spot_price** | **float** |  | 

## Example

```python
from taikunpycore.models.project_details_for_servers_dto import ProjectDetailsForServersDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDetailsForServersDto from a JSON string
project_details_for_servers_dto_instance = ProjectDetailsForServersDto.from_json(json)
# print the JSON string representation of the object
print(ProjectDetailsForServersDto.to_json())

# convert the object into a dict
project_details_for_servers_dto_dict = project_details_for_servers_dto_instance.to_dict()
# create an instance of ProjectDetailsForServersDto from a dict
project_details_for_servers_dto_from_dict = ProjectDetailsForServersDto.from_dict(project_details_for_servers_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


