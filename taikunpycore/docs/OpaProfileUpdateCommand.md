# OpaProfileUpdateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**forbid_node_port** | **bool** |  | [optional] 
**forbid_http_ingress** | **bool** |  | [optional] 
**require_probe** | **bool** |  | [optional] 
**unique_ingresses** | **bool** |  | [optional] 
**unique_service_selector** | **bool** |  | [optional] 
**is_node_name_forbidden_in_vc** | **bool** |  | [optional] 
**is_master_taint_enforced** | **bool** |  | [optional] 
**allowed_repo** | **List[str]** |  | [optional] 
**forbid_specific_tags** | **List[str]** |  | [optional] 
**ingress_whitelist** | **List[str]** |  | [optional] 
**whitelist_master_taint_namespaces** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.opa_profile_update_command import OpaProfileUpdateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of OpaProfileUpdateCommand from a JSON string
opa_profile_update_command_instance = OpaProfileUpdateCommand.from_json(json)
# print the JSON string representation of the object
print(OpaProfileUpdateCommand.to_json())

# convert the object into a dict
opa_profile_update_command_dict = opa_profile_update_command_instance.to_dict()
# create an instance of OpaProfileUpdateCommand from a dict
opa_profile_update_command_from_dict = OpaProfileUpdateCommand.from_dict(opa_profile_update_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


