# DatastoreListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**datacenter_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.datastore_list_command import DatastoreListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreListCommand from a JSON string
datastore_list_command_instance = DatastoreListCommand.from_json(json)
# print the JSON string representation of the object
print(DatastoreListCommand.to_json())

# convert the object into a dict
datastore_list_command_dict = datastore_list_command_instance.to_dict()
# create an instance of DatastoreListCommand from a dict
datastore_list_command_from_dict = DatastoreListCommand.from_dict(datastore_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


