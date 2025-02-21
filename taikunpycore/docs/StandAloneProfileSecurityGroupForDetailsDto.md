# StandAloneProfileSecurityGroupForDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**protocol** | **str** |  | 
**port_min_range** | **int** |  | 
**port_max_range** | **int** |  | 
**remote_ip_prefix** | **str** |  | 
**is_rdp_port_enabled** | **bool** |  | 

## Example

```python
from taikunpycore.models.stand_alone_profile_security_group_for_details_dto import StandAloneProfileSecurityGroupForDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneProfileSecurityGroupForDetailsDto from a JSON string
stand_alone_profile_security_group_for_details_dto_instance = StandAloneProfileSecurityGroupForDetailsDto.from_json(json)
# print the JSON string representation of the object
print(StandAloneProfileSecurityGroupForDetailsDto.to_json())

# convert the object into a dict
stand_alone_profile_security_group_for_details_dto_dict = stand_alone_profile_security_group_for_details_dto_instance.to_dict()
# create an instance of StandAloneProfileSecurityGroupForDetailsDto from a dict
stand_alone_profile_security_group_for_details_dto_from_dict = StandAloneProfileSecurityGroupForDetailsDto.from_dict(stand_alone_profile_security_group_for_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


