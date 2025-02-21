# EditSecurityGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**port_min_range** | **int** |  | [optional] 
**port_max_range** | **int** |  | [optional] 
**remote_ip_prefix** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.edit_security_group_command import EditSecurityGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of EditSecurityGroupCommand from a JSON string
edit_security_group_command_instance = EditSecurityGroupCommand.from_json(json)
# print the JSON string representation of the object
print(EditSecurityGroupCommand.to_json())

# convert the object into a dict
edit_security_group_command_dict = edit_security_group_command_instance.to_dict()
# create an instance of EditSecurityGroupCommand from a dict
edit_security_group_command_from_dict = EditSecurityGroupCommand.from_dict(edit_security_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


