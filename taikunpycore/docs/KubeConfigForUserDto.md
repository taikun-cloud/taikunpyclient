# KubeConfigForUserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**user_id** | **str** |  | 
**display_name** | **str** |  | 
**project_id** | **int** |  | 
**organization_id** | **int** |  | 
**partner_id** | **int** |  | 
**project_name** | **str** |  | 
**is_accessible_for_all** | **bool** |  | 
**is_accessible_for_manager** | **bool** |  | 
**kube_config_role_name** | **str** |  | 
**created_by** | **str** |  | 
**created_at** | **str** |  | 
**namespace** | **str** |  | 
**expiration_date** | **str** |  | 
**can_download** | **bool** |  | 
**can_access_terminal** | **bool** |  | 
**can_delete** | **bool** |  | 

## Example

```python
from taikunpycore.models.kube_config_for_user_dto import KubeConfigForUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubeConfigForUserDto from a JSON string
kube_config_for_user_dto_instance = KubeConfigForUserDto.from_json(json)
# print the JSON string representation of the object
print(KubeConfigForUserDto.to_json())

# convert the object into a dict
kube_config_for_user_dto_dict = kube_config_for_user_dto_instance.to_dict()
# create an instance of KubeConfigForUserDto from a dict
kube_config_for_user_dto_from_dict = KubeConfigForUserDto.from_dict(kube_config_for_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


