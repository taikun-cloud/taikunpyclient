# StandAloneProfileForDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**public_key** | **str** |  | 
**security_groups** | [**List[StandAloneProfileSecurityGroupForDetailsDto]**](StandAloneProfileSecurityGroupForDetailsDto.md) |  | 

## Example

```python
from taikunpycore.models.stand_alone_profile_for_details_dto import StandAloneProfileForDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneProfileForDetailsDto from a JSON string
stand_alone_profile_for_details_dto_instance = StandAloneProfileForDetailsDto.from_json(json)
# print the JSON string representation of the object
print(StandAloneProfileForDetailsDto.to_json())

# convert the object into a dict
stand_alone_profile_for_details_dto_dict = stand_alone_profile_for_details_dto_instance.to_dict()
# create an instance of StandAloneProfileForDetailsDto from a dict
stand_alone_profile_for_details_dto_from_dict = StandAloneProfileForDetailsDto.from_dict(stand_alone_profile_for_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


