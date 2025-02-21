# VClusterActionVisibilityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attach_alerting_profile** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**detach_alerting_profile** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**project_maintenance_mode** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**lock** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**unlock** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 

## Example

```python
from taikunpycore.models.v_cluster_action_visibility_dto import VClusterActionVisibilityDto

# TODO update the JSON string below
json = "{}"
# create an instance of VClusterActionVisibilityDto from a JSON string
v_cluster_action_visibility_dto_instance = VClusterActionVisibilityDto.from_json(json)
# print the JSON string representation of the object
print(VClusterActionVisibilityDto.to_json())

# convert the object into a dict
v_cluster_action_visibility_dto_dict = v_cluster_action_visibility_dto_instance.to_dict()
# create an instance of VClusterActionVisibilityDto from a dict
v_cluster_action_visibility_dto_from_dict = VClusterActionVisibilityDto.from_dict(v_cluster_action_visibility_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


