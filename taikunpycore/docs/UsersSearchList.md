# UsersSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UsersSearchResponseData]**](UsersSearchResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.users_search_list import UsersSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of UsersSearchList from a JSON string
users_search_list_instance = UsersSearchList.from_json(json)
# print the JSON string representation of the object
print(UsersSearchList.to_json())

# convert the object into a dict
users_search_list_dict = users_search_list_instance.to_dict()
# create an instance of UsersSearchList from a dict
users_search_list_from_dict = UsersSearchList.from_dict(users_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


