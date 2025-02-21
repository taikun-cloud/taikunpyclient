# VClusterListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_virtual_cluster** | **bool** |  | 
**is_locked** | **bool** |  | 
**has_kube_config_file** | **bool** |  | 
**is_maintenance_mode_enabled** | **bool** |  | 
**organization_name** | **str** |  | 
**organization_id** | **int** |  | 
**kubernetes_version** | **str** |  | 
**created_at** | **str** |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**alerts_count** | **int** |  | 
**expired_at** | **str** |  | 
**delete_on_expiration** | **bool** |  | 
**wasm_enabled** | **bool** |  | 
**alerting_profile_id** | **int** |  | 
**alerting_profile_name** | **str** |  | 
**access_ip** | **str** |  | 
**cloud_type** | [**CloudType**](CloudType.md) |  | 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | 
**health** | [**ProjectHealth**](ProjectHealth.md) |  | 
**lock_button** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**unlock_button** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**delete_button** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**kube_info_button** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**set_expiration_date_button** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**reset_status_button** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 

## Example

```python
from taikunpycore.models.v_cluster_list_dto import VClusterListDto

# TODO update the JSON string below
json = "{}"
# create an instance of VClusterListDto from a JSON string
v_cluster_list_dto_instance = VClusterListDto.from_json(json)
# print the JSON string representation of the object
print(VClusterListDto.to_json())

# convert the object into a dict
v_cluster_list_dto_dict = v_cluster_list_dto_instance.to_dict()
# create an instance of VClusterListDto from a dict
v_cluster_list_dto_from_dict = VClusterListDto.from_dict(v_cluster_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


