# StandAloneVmDiskDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**volume_type** | **str** |  | [optional] 
**device_name** | **str** |  | [optional] 
**lun_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.stand_alone_vm_disk_dto import StandAloneVmDiskDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneVmDiskDto from a JSON string
stand_alone_vm_disk_dto_instance = StandAloneVmDiskDto.from_json(json)
# print the JSON string representation of the object
print(StandAloneVmDiskDto.to_json())

# convert the object into a dict
stand_alone_vm_disk_dto_dict = stand_alone_vm_disk_dto_instance.to_dict()
# create an instance of StandAloneVmDiskDto from a dict
stand_alone_vm_disk_dto_from_dict = StandAloneVmDiskDto.from_dict(stand_alone_vm_disk_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


