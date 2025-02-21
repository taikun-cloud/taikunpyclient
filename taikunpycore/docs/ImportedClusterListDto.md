# ImportedClusterListDto


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

## Example

```python
from taikunpycore.models.imported_cluster_list_dto import ImportedClusterListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedClusterListDto from a JSON string
imported_cluster_list_dto_instance = ImportedClusterListDto.from_json(json)
# print the JSON string representation of the object
print(ImportedClusterListDto.to_json())

# convert the object into a dict
imported_cluster_list_dto_dict = imported_cluster_list_dto_instance.to_dict()
# create an instance of ImportedClusterListDto from a dict
imported_cluster_list_dto_from_dict = ImportedClusterListDto.from_dict(imported_cluster_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


