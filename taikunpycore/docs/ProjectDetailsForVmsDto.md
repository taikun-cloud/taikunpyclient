# ProjectDetailsForVmsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**ProjectStatus**](ProjectStatus.md) |  | 
**name** | **str** |  | 
**id** | **int** |  | 
**cloud_type** | [**CloudType**](CloudType.md) |  | 
**cloud_name** | **str** |  | 
**cloud_id** | **int** |  | 
**organization_name** | **str** |  | 
**organization_id** | **int** |  | 
**is_locked** | **bool** |  | 
**is_project_maintenance_mode_enabled** | **bool** |  | 
**has_selected_flavors** | **bool** |  | 
**is_maintenance_mode_enabled** | **bool** |  | 
**is_drs_enabled** | **bool** |  | 
**project_cloud_revision** | **int** |  | 
**cloud_credential_revision** | **int** |  | 
**allow_full_spot_kubernetes** | **bool** |  | 
**allow_spot_workers** | **bool** |  | 
**allow_spot_vms** | **bool** |  | 
**max_spot_price** | **float** |  | 
**total_hourly_cost** | **float** |  | 
**availability_zones** | **List[str]** |  | 
**hypervisors** | **List[str]** |  | 
**expired_at** | **str** |  | 

## Example

```python
from taikunpycore.models.project_details_for_vms_dto import ProjectDetailsForVmsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDetailsForVmsDto from a JSON string
project_details_for_vms_dto_instance = ProjectDetailsForVmsDto.from_json(json)
# print the JSON string representation of the object
print(ProjectDetailsForVmsDto.to_json())

# convert the object into a dict
project_details_for_vms_dto_dict = project_details_for_vms_dto_instance.to_dict()
# create an instance of ProjectDetailsForVmsDto from a dict
project_details_for_vms_dto_from_dict = ProjectDetailsForVmsDto.from_dict(project_details_for_vms_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


