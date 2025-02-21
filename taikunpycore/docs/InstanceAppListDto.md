# InstanceAppListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**namespace** | **str** |  | 
**status** | [**EInstanceStatus**](EInstanceStatus.md) |  | 
**version** | **str** |  | 
**catalog_id** | **int** |  | 
**catalog_name** | **str** |  | 
**catalog_app_name** | **str** |  | 
**catalog_app_id** | **int** |  | 
**app_repo_name** | **str** |  | 
**logo** | **str** |  | 
**auto_sync** | **bool** |  | 
**created** | **str** |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**project_id** | **int** |  | 
**project_name** | **str** |  | 
**logs** | **str** |  | 

## Example

```python
from taikunpycore.models.instance_app_list_dto import InstanceAppListDto

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceAppListDto from a JSON string
instance_app_list_dto_instance = InstanceAppListDto.from_json(json)
# print the JSON string representation of the object
print(InstanceAppListDto.to_json())

# convert the object into a dict
instance_app_list_dto_dict = instance_app_list_dto_instance.to_dict()
# create an instance of InstanceAppListDto from a dict
instance_app_list_dto_from_dict = InstanceAppListDto.from_dict(instance_app_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


