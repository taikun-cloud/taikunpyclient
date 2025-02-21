# StandAloneVmDiskForDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**current_size** | **int** |  | 
**target_size** | **int** |  | 
**volume_type** | **str** |  | 
**device_name** | **str** |  | 
**lun_id** | **str** |  | 
**status** | [**StandAloneVmDiskStatus**](StandAloneVmDiskStatus.md) |  | 

## Example

```python
from taikunpycore.models.stand_alone_vm_disk_for_details_dto import StandAloneVmDiskForDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneVmDiskForDetailsDto from a JSON string
stand_alone_vm_disk_for_details_dto_instance = StandAloneVmDiskForDetailsDto.from_json(json)
# print the JSON string representation of the object
print(StandAloneVmDiskForDetailsDto.to_json())

# convert the object into a dict
stand_alone_vm_disk_for_details_dto_dict = stand_alone_vm_disk_for_details_dto_instance.to_dict()
# create an instance of StandAloneVmDiskForDetailsDto from a dict
stand_alone_vm_disk_for_details_dto_from_dict = StandAloneVmDiskForDetailsDto.from_dict(stand_alone_vm_disk_for_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


