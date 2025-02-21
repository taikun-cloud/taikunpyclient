# ServersListForDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServerListDto]**](ServerListDto.md) |  | 
**project** | [**ProjectDetailsForServersDto**](ProjectDetailsForServersDto.md) |  | 

## Example

```python
from taikunpycore.models.servers_list_for_details import ServersListForDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ServersListForDetails from a JSON string
servers_list_for_details_instance = ServersListForDetails.from_json(json)
# print the JSON string representation of the object
print(ServersListForDetails.to_json())

# convert the object into a dict
servers_list_for_details_dict = servers_list_for_details_instance.to_dict()
# create an instance of ServersListForDetails from a dict
servers_list_for_details_from_dict = ServersListForDetails.from_dict(servers_list_for_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


