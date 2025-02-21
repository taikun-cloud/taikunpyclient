# ProjectListDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_kubernetes** | **bool** |  | 
**is_locked** | **bool** |  | 
**is_virtual_cluster** | **bool** |  | 
**is_monitoring_enabled** | **bool** |  | 
**has_kube_config_file** | **bool** |  | 
**is_maintenance_mode_enabled** | **bool** |  | 
**cloud_credential_name** | **str** |  | [optional] 
**organization_name** | **str** |  | 
**organization_id** | **int** |  | 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | 
**health** | [**ProjectHealth**](ProjectHealth.md) |  | 
**cloud_type** | [**CloudType**](CloudType.md) |  | [optional] 
**kubespray_current_version** | **str** |  | 
**kubespray_target_version** | **str** |  | 
**kubernetes_current_version** | **str** |  | 
**kubernetes_target_version** | **str** |  | 
**created_at** | **str** |  | 
**alerts_count** | **int** |  | 
**total_servers_count** | **int** |  | 
**total_standalone_vms_count** | **int** |  | 
**bound_users** | [**List[UserDto]**](UserDto.md) |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**expired_at** | **str** |  | 
**delete_on_expiration** | **bool** |  | 
**certificate_expired_at** | **str** |  | 
**last_modified_by** | **str** |  | 
**quota_id** | **int** |  | 
**allow_full_spot_kubernetes** | **bool** |  | 
**allow_spot_workers** | **bool** |  | 
**allow_spot_vms** | **bool** |  | 
**max_spot_price** | **float** |  | 
**project_action** | **bool** |  | 
**has_expiration_warning** | **bool** |  | 
**total_hourly_cost** | **float** |  | 
**is_autoscaling_enabled** | **bool** |  | 
**is_autoscaling_spot_enabled** | **bool** |  | 
**ai_enabled** | **bool** |  | 
**any_server** | **bool** |  | 
**any_vm** | **bool** |  | 
**is_backup_enabled** | **bool** |  | 
**is_project_maintenance_mode_enabled** | **bool** |  | 
**all_users** | **List[str]** |  | 
**parent_project_id** | **int** |  | 
**alerting_profile_id** | **int** |  | 
**opa_profile_id** | **int** |  | 
**lock_button** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | [optional] 
**unlock_button** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | [optional] 
**delete_button** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | [optional] 
**kube_info_button** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | [optional] 
**set_expiration_date_button** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | [optional] 
**reset_status_button** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | [optional] 
**import_cluster_type** | [**ImportClusterType**](ImportClusterType.md) |  | 
**e_import_cluster_type** | [**EImportClusterType**](EImportClusterType.md) |  | [optional] 

## Example

```python
from taikunpycore.models.project_list_detail_dto import ProjectListDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectListDetailDto from a JSON string
project_list_detail_dto_instance = ProjectListDetailDto.from_json(json)
# print the JSON string representation of the object
print(ProjectListDetailDto.to_json())

# convert the object into a dict
project_list_detail_dto_dict = project_list_detail_dto_instance.to_dict()
# create an instance of ProjectListDetailDto from a dict
project_list_detail_dto_from_dict = ProjectListDetailDto.from_dict(project_list_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


