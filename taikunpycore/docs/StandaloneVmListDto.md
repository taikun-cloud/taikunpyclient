# StandaloneVmListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**flavor_id** | **str** |  | 
**volume_size** | **int** |  | 
**organization_name** | **str** |  | 
**organization_id** | **int** |  | 
**ram** | **int** |  | 
**cpu** | **int** |  | 
**volume_type** | **str** |  | 
**public_ip_enabled** | **bool** |  | 
**public_ip** | **str** |  | 
**ip_address** | **str** |  | 
**cloud_type** | [**CloudType**](CloudType.md) |  | 
**image_name** | **str** |  | 
**revision** | **int** |  | 
**is_windows** | **bool** |  | 
**status** | [**StandAloneVmStatus**](StandAloneVmStatus.md) |  | 
**project_name** | **str** |  | 
**project_id** | **int** |  | 
**stand_alone_profile** | [**StandaloneProfileListDto**](StandaloneProfileListDto.md) |  | 
**created_at** | **str** |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 

## Example

```python
from taikunpycore.models.standalone_vm_list_dto import StandaloneVmListDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandaloneVmListDto from a JSON string
standalone_vm_list_dto_instance = StandaloneVmListDto.from_json(json)
# print the JSON string representation of the object
print(StandaloneVmListDto.to_json())

# convert the object into a dict
standalone_vm_list_dto_dict = standalone_vm_list_dto_instance.to_dict()
# create an instance of StandaloneVmListDto from a dict
standalone_vm_list_dto_from_dict = StandaloneVmListDto.from_dict(standalone_vm_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


