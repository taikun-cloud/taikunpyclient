# AccessProfilesSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CommonSearchResponseData]**](CommonSearchResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.access_profiles_search_list import AccessProfilesSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfilesSearchList from a JSON string
access_profiles_search_list_instance = AccessProfilesSearchList.from_json(json)
# print the JSON string representation of the object
print(AccessProfilesSearchList.to_json())

# convert the object into a dict
access_profiles_search_list_dict = access_profiles_search_list_instance.to_dict()
# create an instance of AccessProfilesSearchList from a dict
access_profiles_search_list_from_dict = AccessProfilesSearchList.from_dict(access_profiles_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


