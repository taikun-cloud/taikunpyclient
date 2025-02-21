# StandAloneProfilesSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchResponseData]**](CommonSearchResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.stand_alone_profiles_search_list import StandAloneProfilesSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneProfilesSearchList from a JSON string
stand_alone_profiles_search_list_instance = StandAloneProfilesSearchList.from_json(json)
# print the JSON string representation of the object
print(StandAloneProfilesSearchList.to_json())

# convert the object into a dict
stand_alone_profiles_search_list_dict = stand_alone_profiles_search_list_instance.to_dict()
# create an instance of StandAloneProfilesSearchList from a dict
stand_alone_profiles_search_list_from_dict = StandAloneProfilesSearchList.from_dict(stand_alone_profiles_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


