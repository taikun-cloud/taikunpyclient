# OpenstackNetworkDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_limit** | **int** |  | [optional] 
**subnet_limit** | **int** |  | [optional] 
**floating_ip_limit** | **int** |  | [optional] 
**router_limit** | **int** |  | [optional] 
**security_group_limit** | **int** |  | [optional] 
**security_group_rule_limit** | **int** |  | [optional] 
**port_limit** | **int** |  | [optional] 
**network_used** | **int** |  | [optional] 
**subnet_used** | **int** |  | [optional] 
**floating_ip_used** | **int** |  | [optional] 
**router_used** | **int** |  | [optional] 
**security_group_used** | **int** |  | [optional] 
**port_used** | **int** |  | [optional] 
**security_group_rule_used** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.openstack_network_dto import OpenstackNetworkDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenstackNetworkDto from a JSON string
openstack_network_dto_instance = OpenstackNetworkDto.from_json(json)
# print the JSON string representation of the object
print(OpenstackNetworkDto.to_json())

# convert the object into a dict
openstack_network_dto_dict = openstack_network_dto_instance.to_dict()
# create an instance of OpenstackNetworkDto from a dict
openstack_network_dto_from_dict = OpenstackNetworkDto.from_dict(openstack_network_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


