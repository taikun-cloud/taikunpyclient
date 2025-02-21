# SecurityGroupListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**protocol** | **str** |  | 
**port_min_range** | **int** |  | 
**port_max_range** | **int** |  | 
**remote_ip_prefix** | **str** |  | 
**profile_name** | **str** |  | 

## Example

```python
from taikunpycore.models.security_group_list_dto import SecurityGroupListDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityGroupListDto from a JSON string
security_group_list_dto_instance = SecurityGroupListDto.from_json(json)
# print the JSON string representation of the object
print(SecurityGroupListDto.to_json())

# convert the object into a dict
security_group_list_dto_dict = security_group_list_dto_instance.to_dict()
# create an instance of SecurityGroupListDto from a dict
security_group_list_dto_from_dict = SecurityGroupListDto.from_dict(security_group_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


