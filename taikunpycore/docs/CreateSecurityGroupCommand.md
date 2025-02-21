# CreateSecurityGroupCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**protocol** | [**SecurityGroupProtocol**](SecurityGroupProtocol.md) |  | [optional] 
**port_min_range** | **int** |  | [optional] 
**port_max_range** | **int** |  | [optional] 
**remote_ip_prefix** | **str** |  | [optional] 
**stand_alone_profile_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_security_group_command import CreateSecurityGroupCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSecurityGroupCommand from a JSON string
create_security_group_command_instance = CreateSecurityGroupCommand.from_json(json)
# print the JSON string representation of the object
print(CreateSecurityGroupCommand.to_json())

# convert the object into a dict
create_security_group_command_dict = create_security_group_command_instance.to_dict()
# create an instance of CreateSecurityGroupCommand from a dict
create_security_group_command_from_dict = CreateSecurityGroupCommand.from_dict(create_security_group_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


