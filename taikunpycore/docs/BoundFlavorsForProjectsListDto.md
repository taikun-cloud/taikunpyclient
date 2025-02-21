# BoundFlavorsForProjectsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**cpu** | **int** |  | 
**ram** | **float** |  | 
**project_id** | **int** |  | 
**project_name** | **str** |  | 
**max_data_disk_count** | **int** |  | 
**exists_linux_spot_price** | **bool** |  | 
**exists_windows_spot_price** | **bool** |  | 
**linux_spot_price** | **str** |  | 
**linux_price** | **str** |  | 
**windows_spot_price** | **str** |  | 
**windows_price** | **str** |  | 
**cloud_type** | [**CloudType**](CloudType.md) |  | 

## Example

```python
from taikunpycore.models.bound_flavors_for_projects_list_dto import BoundFlavorsForProjectsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of BoundFlavorsForProjectsListDto from a JSON string
bound_flavors_for_projects_list_dto_instance = BoundFlavorsForProjectsListDto.from_json(json)
# print the JSON string representation of the object
print(BoundFlavorsForProjectsListDto.to_json())

# convert the object into a dict
bound_flavors_for_projects_list_dto_dict = bound_flavors_for_projects_list_dto_instance.to_dict()
# create an instance of BoundFlavorsForProjectsListDto from a dict
bound_flavors_for_projects_list_dto_from_dict = BoundFlavorsForProjectsListDto.from_dict(bound_flavors_for_projects_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


