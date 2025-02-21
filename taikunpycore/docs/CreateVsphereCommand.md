# CreateVsphereCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**datacenter_id** | **str** |  | [optional] 
**datacenter_name** | **str** |  | [optional] 
**datastore_name** | **str** |  | [optional] 
**resource_pool_name** | **str** |  | [optional] 
**drs_enabled** | **bool** |  | [optional] 
**vm_template_name** | **str** |  | [optional] 
**continent** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**hypervisors** | **List[str]** |  | [optional] 
**public_network** | [**CreateVsphereNetworkDto**](CreateVsphereNetworkDto.md) |  | [optional] 
**private_network** | [**CreateVsphereNetworkDto**](CreateVsphereNetworkDto.md) |  | [optional] 
**skip_tls_flag** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.create_vsphere_command import CreateVsphereCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVsphereCommand from a JSON string
create_vsphere_command_instance = CreateVsphereCommand.from_json(json)
# print the JSON string representation of the object
print(CreateVsphereCommand.to_json())

# convert the object into a dict
create_vsphere_command_dict = create_vsphere_command_instance.to_dict()
# create an instance of CreateVsphereCommand from a dict
create_vsphere_command_from_dict = CreateVsphereCommand.from_dict(create_vsphere_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


