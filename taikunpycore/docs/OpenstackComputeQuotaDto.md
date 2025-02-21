# OpenstackComputeQuotaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_total_ram_size** | **int** |  | [optional] 
**max_server_groups** | **int** |  | [optional] 
**max_total_instances** | **int** |  | [optional] 
**max_total_cores** | **int** |  | [optional] 
**used_ram_size** | **int** |  | [optional] 
**used_cpu_size** | **int** |  | [optional] 
**used_instance_size** | **int** |  | [optional] 
**used_server_groups** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.openstack_compute_quota_dto import OpenstackComputeQuotaDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenstackComputeQuotaDto from a JSON string
openstack_compute_quota_dto_instance = OpenstackComputeQuotaDto.from_json(json)
# print the JSON string representation of the object
print(OpenstackComputeQuotaDto.to_json())

# convert the object into a dict
openstack_compute_quota_dto_dict = openstack_compute_quota_dto_instance.to_dict()
# create an instance of OpenstackComputeQuotaDto from a dict
openstack_compute_quota_dto_from_dict = OpenstackComputeQuotaDto.from_dict(openstack_compute_quota_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


