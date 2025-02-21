# ProjectActionVisibilityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**repair** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**upgrade** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**enable_monitoring** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**disable_monitoring** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**enable_backup** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**disable_backup** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**enable_opa** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**disable_opa** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**enable_autoscaler** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**disable_autoscaler** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**vm_repair** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**vm_commit** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**lock** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**unlock** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**enable_spot_worker** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**disable_spot_worker** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**enable_full_spot** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**disable_full_spot** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**enable_spot_vm** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**disable_spot_vm** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**attach_alerting_profile** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**detach_alerting_profile** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**enable_ai** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**disable_ai** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**ai_assistant** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**project_maintenance_mode** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**add_server** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**add_vm** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 

## Example

```python
from taikunpycore.models.project_action_visibility_dto import ProjectActionVisibilityDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectActionVisibilityDto from a JSON string
project_action_visibility_dto_instance = ProjectActionVisibilityDto.from_json(json)
# print the JSON string representation of the object
print(ProjectActionVisibilityDto.to_json())

# convert the object into a dict
project_action_visibility_dto_dict = project_action_visibility_dto_instance.to_dict()
# create an instance of ProjectActionVisibilityDto from a dict
project_action_visibility_dto_from_dict = ProjectActionVisibilityDto.from_dict(project_action_visibility_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


