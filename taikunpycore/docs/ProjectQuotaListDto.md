# ProjectQuotaListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_cpu** | **int** |  | 
**server_ram** | **float** |  | 
**server_disk_size** | **float** |  | 
**vm_cpu** | **int** |  | 
**vm_ram** | **float** |  | 
**vm_volume_size** | **float** |  | 
**project_id** | **int** |  | 
**project_name** | **str** |  | 

## Example

```python
from taikunpycore.models.project_quota_list_dto import ProjectQuotaListDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectQuotaListDto from a JSON string
project_quota_list_dto_instance = ProjectQuotaListDto.from_json(json)
# print the JSON string representation of the object
print(ProjectQuotaListDto.to_json())

# convert the object into a dict
project_quota_list_dto_dict = project_quota_list_dto_instance.to_dict()
# create an instance of ProjectQuotaListDto from a dict
project_quota_list_dto_from_dict = ProjectQuotaListDto.from_dict(project_quota_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


