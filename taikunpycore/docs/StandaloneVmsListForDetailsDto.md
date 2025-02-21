# StandaloneVmsListForDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**image_name** | **str** |  | 
**image_id** | **str** |  | 
**status** | **str** |  | 
**cloud_init** | **str** |  | 
**volume_type** | **str** |  | 
**volume_size** | **int** |  | 
**created_at** | **str** |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**ssh_public_key** | **str** |  | 
**current_flavor** | **str** |  | 
**target_flavor** | **str** |  | 
**public_ip_enabled** | **bool** |  | 
**public_ip** | **str** |  | 
**hypervisor** | **str** |  | 
**hypervisor_id** | **str** |  | 
**ip_address** | **str** |  | 
**spot_price** | **float** |  | 
**spot_instance** | **bool** |  | 
**availability_zone** | **str** |  | 
**action_buttons** | [**StandaloneVisibilityDto**](StandaloneVisibilityDto.md) |  | 
**is_windows** | **bool** |  | 
**disks** | [**List[StandAloneVmDiskForDetailsDto]**](StandAloneVmDiskForDetailsDto.md) |  | 
**stand_alone_meta_datas** | [**List[StandAloneMetaDataDtoForVm]**](StandAloneMetaDataDtoForVm.md) |  | 
**profile** | [**StandAloneProfileForDetailsDto**](StandAloneProfileForDetailsDto.md) |  | 

## Example

```python
from taikunpycore.models.standalone_vms_list_for_details_dto import StandaloneVmsListForDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandaloneVmsListForDetailsDto from a JSON string
standalone_vms_list_for_details_dto_instance = StandaloneVmsListForDetailsDto.from_json(json)
# print the JSON string representation of the object
print(StandaloneVmsListForDetailsDto.to_json())

# convert the object into a dict
standalone_vms_list_for_details_dto_dict = standalone_vms_list_for_details_dto_instance.to_dict()
# create an instance of StandaloneVmsListForDetailsDto from a dict
standalone_vms_list_for_details_dto_from_dict = StandaloneVmsListForDetailsDto.from_dict(standalone_vms_list_for_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


