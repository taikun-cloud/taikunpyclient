# CommonDropdownIsBoundDtoForProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**is_bound** | **bool** |  | [optional] 
**has_kube_config_file** | **bool** |  | [optional] 
**kubernetes_version** | **str** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**maintenance_mode_enabled** | **bool** |  | [optional] 
**is_virtual_cluster** | **bool** |  | [optional] 
**alerting_profile_id** | **int** |  | [optional] 
**cloud_type** | [**CloudType**](CloudType.md) |  | [optional] 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | [optional] 
**health** | [**ProjectHealth**](ProjectHealth.md) |  | [optional] 
**import_cluster_type** | [**ImportClusterType**](ImportClusterType.md) |  | [optional] 

## Example

```python
from taikunpycore.models.common_dropdown_is_bound_dto_for_project import CommonDropdownIsBoundDtoForProject

# TODO update the JSON string below
json = "{}"
# create an instance of CommonDropdownIsBoundDtoForProject from a JSON string
common_dropdown_is_bound_dto_for_project_instance = CommonDropdownIsBoundDtoForProject.from_json(json)
# print the JSON string representation of the object
print(CommonDropdownIsBoundDtoForProject.to_json())

# convert the object into a dict
common_dropdown_is_bound_dto_for_project_dict = common_dropdown_is_bound_dto_for_project_instance.to_dict()
# create an instance of CommonDropdownIsBoundDtoForProject from a dict
common_dropdown_is_bound_dto_for_project_from_dict = CommonDropdownIsBoundDtoForProject.from_dict(common_dropdown_is_bound_dto_for_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


