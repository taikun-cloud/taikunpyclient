# StandAloneProfileSecurityGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**protocol** | [**SecurityGroupProtocol**](SecurityGroupProtocol.md) |  | [optional] 
**port_min_range** | **int** |  | [optional] 
**port_max_range** | **int** |  | [optional] 
**remote_ip_prefix** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.stand_alone_profile_security_group_dto import StandAloneProfileSecurityGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneProfileSecurityGroupDto from a JSON string
stand_alone_profile_security_group_dto_instance = StandAloneProfileSecurityGroupDto.from_json(json)
# print the JSON string representation of the object
print(StandAloneProfileSecurityGroupDto.to_json())

# convert the object into a dict
stand_alone_profile_security_group_dto_dict = stand_alone_profile_security_group_dto_instance.to_dict()
# create an instance of StandAloneProfileSecurityGroupDto from a dict
stand_alone_profile_security_group_dto_from_dict = StandAloneProfileSecurityGroupDto.from_dict(stand_alone_profile_security_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


