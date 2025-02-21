# AccessProfilesList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AccessProfilesListDto]**](AccessProfilesListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.access_profiles_list import AccessProfilesList

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfilesList from a JSON string
access_profiles_list_instance = AccessProfilesList.from_json(json)
# print the JSON string representation of the object
print(AccessProfilesList.to_json())

# convert the object into a dict
access_profiles_list_dict = access_profiles_list_instance.to_dict()
# create an instance of AccessProfilesList from a dict
access_profiles_list_from_dict = AccessProfilesList.from_dict(access_profiles_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


