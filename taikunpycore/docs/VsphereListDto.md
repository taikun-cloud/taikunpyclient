# VsphereListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**project_count** | **int** |  | 
**is_locked** | **bool** |  | 
**name** | **str** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**created_by** | **str** |  | 
**created_at** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**is_default** | **bool** |  | 
**drs_enabled** | **bool** |  | 
**resource_pool** | **str** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**continent_name** | **str** |  | 
**hypervisors** | [**List[CommonStringBasedDropdownDto]**](CommonStringBasedDropdownDto.md) |  | 
**username** | **str** |  | 
**url** | **str** |  | 
**datacenter_id** | **str** |  | 
**datacenter_name** | **str** |  | 
**datastore** | **str** |  | 
**vm_template_name** | **str** |  | 
**vsphere_networks** | [**List[VsphereNetworkListDto]**](VsphereNetworkListDto.md) |  | 
**skip_tls_flag** | **bool** |  | 

## Example

```python
from taikunpycore.models.vsphere_list_dto import VsphereListDto

# TODO update the JSON string below
json = "{}"
# create an instance of VsphereListDto from a JSON string
vsphere_list_dto_instance = VsphereListDto.from_json(json)
# print the JSON string representation of the object
print(VsphereListDto.to_json())

# convert the object into a dict
vsphere_list_dto_dict = vsphere_list_dto_instance.to_dict()
# create an instance of VsphereListDto from a dict
vsphere_list_dto_from_dict = VsphereListDto.from_dict(vsphere_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


