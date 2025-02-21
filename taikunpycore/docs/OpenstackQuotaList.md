# OpenstackQuotaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute** | [**OpenstackComputeQuotaDto**](OpenstackComputeQuotaDto.md) |  | [optional] 
**volume** | [**OpenstackVolumeQuotaDto**](OpenstackVolumeQuotaDto.md) |  | [optional] 
**network** | [**OpenstackNetworkDto**](OpenstackNetworkDto.md) |  | [optional] 
**is_infra** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.openstack_quota_list import OpenstackQuotaList

# TODO update the JSON string below
json = "{}"
# create an instance of OpenstackQuotaList from a JSON string
openstack_quota_list_instance = OpenstackQuotaList.from_json(json)
# print the JSON string representation of the object
print(OpenstackQuotaList.to_json())

# convert the object into a dict
openstack_quota_list_dict = openstack_quota_list_instance.to_dict()
# create an instance of OpenstackQuotaList from a dict
openstack_quota_list_from_dict = OpenstackQuotaList.from_dict(openstack_quota_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


