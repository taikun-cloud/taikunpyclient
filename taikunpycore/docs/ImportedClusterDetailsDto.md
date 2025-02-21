# ImportedClusterDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**is_locked** | **bool** |  | 
**access_ip** | **str** |  | 
**kubernetes_version** | **str** |  | 
**import_cluster_type** | [**ImportClusterType**](ImportClusterType.md) |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**cloud_credential_name** | **str** |  | [optional] 
**cloud_credential_id** | **int** |  | [optional] 
**health** | [**ProjectHealth**](ProjectHealth.md) |  | 
**cloud_type** | [**CloudType**](CloudType.md) |  | [optional] 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | 
**is_monitoring_enabled** | **bool** |  | 
**alerting_profile_id** | **int** |  | 
**alerting_profile_name** | **str** |  | 
**is_opa_enabled** | **bool** |  | 
**opa_profile_id** | **int** |  | 
**is_backup_enabled** | **bool** |  | 
**s3_credential_id** | **int** |  | 
**ai_enabled** | **bool** |  | 
**ai_credential_id** | **int** |  | 
**expired_at** | **str** |  | 
**alerts_count** | **int** |  | 

## Example

```python
from taikunpycore.models.imported_cluster_details_dto import ImportedClusterDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedClusterDetailsDto from a JSON string
imported_cluster_details_dto_instance = ImportedClusterDetailsDto.from_json(json)
# print the JSON string representation of the object
print(ImportedClusterDetailsDto.to_json())

# convert the object into a dict
imported_cluster_details_dto_dict = imported_cluster_details_dto_instance.to_dict()
# create an instance of ImportedClusterDetailsDto from a dict
imported_cluster_details_dto_from_dict = ImportedClusterDetailsDto.from_dict(imported_cluster_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


