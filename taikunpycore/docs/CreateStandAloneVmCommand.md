# CreateStandAloneVmCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flavor_name** | **str** |  | [optional] 
**volume_size** | **int** |  | [optional] 
**volume_type** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**public_ip_enabled** | **bool** |  | [optional] 
**image** | **str** |  | [optional] 
**cloud_init** | **str** |  | [optional] 
**stand_alone_profile_id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**spot_price** | **float** |  | [optional] 
**spot_instance** | **bool** |  | [optional] 
**availability_zone** | **str** |  | [optional] 
**hypervisor** | **str** |  | [optional] 
**stand_alone_vm_disks** | [**List[StandAloneVmDiskDto]**](StandAloneVmDiskDto.md) |  | [optional] 
**stand_alone_meta_datas** | [**List[StandAloneMetaDataDto]**](StandAloneMetaDataDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.create_stand_alone_vm_command import CreateStandAloneVmCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStandAloneVmCommand from a JSON string
create_stand_alone_vm_command_instance = CreateStandAloneVmCommand.from_json(json)
# print the JSON string representation of the object
print(CreateStandAloneVmCommand.to_json())

# convert the object into a dict
create_stand_alone_vm_command_dict = create_stand_alone_vm_command_instance.to_dict()
# create an instance of CreateStandAloneVmCommand from a dict
create_stand_alone_vm_command_from_dict = CreateStandAloneVmCommand.from_dict(create_stand_alone_vm_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


