# StandAloneProfilesListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**public_key** | **str** |  | 
**is_locked** | **bool** |  | 
**standalone_vms** | [**List[StandAloneVmSmallDetailDto]**](StandAloneVmSmallDetailDto.md) |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**partner_logo** | **str** |  | 
**created_at** | **str** |  | 

## Example

```python
from taikunpycore.models.stand_alone_profiles_list_dto import StandAloneProfilesListDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneProfilesListDto from a JSON string
stand_alone_profiles_list_dto_instance = StandAloneProfilesListDto.from_json(json)
# print the JSON string representation of the object
print(StandAloneProfilesListDto.to_json())

# convert the object into a dict
stand_alone_profiles_list_dto_dict = stand_alone_profiles_list_dto_instance.to_dict()
# create an instance of StandAloneProfilesListDto from a dict
stand_alone_profiles_list_dto_from_dict = StandAloneProfilesListDto.from_dict(stand_alone_profiles_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


