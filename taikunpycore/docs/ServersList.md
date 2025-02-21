# ServersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServerListDto]**](ServerListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.servers_list import ServersList

# TODO update the JSON string below
json = "{}"
# create an instance of ServersList from a JSON string
servers_list_instance = ServersList.from_json(json)
# print the JSON string representation of the object
print(ServersList.to_json())

# convert the object into a dict
servers_list_dict = servers_list_instance.to_dict()
# create an instance of ServersList from a dict
servers_list_from_dict = ServersList.from_dict(servers_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


