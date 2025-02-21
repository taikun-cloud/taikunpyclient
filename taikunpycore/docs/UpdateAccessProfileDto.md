# UpdateAccessProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**http_proxy** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_access_profile_dto import UpdateAccessProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAccessProfileDto from a JSON string
update_access_profile_dto_instance = UpdateAccessProfileDto.from_json(json)
# print the JSON string representation of the object
print(UpdateAccessProfileDto.to_json())

# convert the object into a dict
update_access_profile_dto_dict = update_access_profile_dto_instance.to_dict()
# create an instance of UpdateAccessProfileDto from a dict
update_access_profile_dto_from_dict = UpdateAccessProfileDto.from_dict(update_access_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


