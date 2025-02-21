# UsersSearchResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.users_search_response_data import UsersSearchResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UsersSearchResponseData from a JSON string
users_search_response_data_instance = UsersSearchResponseData.from_json(json)
# print the JSON string representation of the object
print(UsersSearchResponseData.to_json())

# convert the object into a dict
users_search_response_data_dict = users_search_response_data_instance.to_dict()
# create an instance of UsersSearchResponseData from a dict
users_search_response_data_from_dict = UsersSearchResponseData.from_dict(users_search_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


