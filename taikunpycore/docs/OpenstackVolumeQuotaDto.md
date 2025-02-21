# OpenstackVolumeQuotaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_total_volume_size** | **int** |  | [optional] 
**used_volume_size** | **int** |  | [optional] 
**max_count_volume_size** | **int** |  | [optional] 
**count_volume_size** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.openstack_volume_quota_dto import OpenstackVolumeQuotaDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenstackVolumeQuotaDto from a JSON string
openstack_volume_quota_dto_instance = OpenstackVolumeQuotaDto.from_json(json)
# print the JSON string representation of the object
print(OpenstackVolumeQuotaDto.to_json())

# convert the object into a dict
openstack_volume_quota_dto_dict = openstack_volume_quota_dto_instance.to_dict()
# create an instance of OpenstackVolumeQuotaDto from a dict
openstack_volume_quota_dto_from_dict = OpenstackVolumeQuotaDto.from_dict(openstack_volume_quota_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


