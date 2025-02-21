# ServersSearchList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServersSearchResponseData]**](ServersSearchResponseData.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.servers_search_list import ServersSearchList

# TODO update the JSON string below
json = "{}"
# create an instance of ServersSearchList from a JSON string
servers_search_list_instance = ServersSearchList.from_json(json)
# print the JSON string representation of the object
print(ServersSearchList.to_json())

# convert the object into a dict
servers_search_list_dict = servers_search_list_instance.to_dict()
# create an instance of ServersSearchList from a dict
servers_search_list_from_dict = ServersSearchList.from_dict(servers_search_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


