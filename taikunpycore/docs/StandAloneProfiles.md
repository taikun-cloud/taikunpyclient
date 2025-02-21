# StandAloneProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[StandAloneProfilesListDto]**](StandAloneProfilesListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.stand_alone_profiles import StandAloneProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneProfiles from a JSON string
stand_alone_profiles_instance = StandAloneProfiles.from_json(json)
# print the JSON string representation of the object
print(StandAloneProfiles.to_json())

# convert the object into a dict
stand_alone_profiles_dict = stand_alone_profiles_instance.to_dict()
# create an instance of StandAloneProfiles from a dict
stand_alone_profiles_from_dict = StandAloneProfiles.from_dict(stand_alone_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


