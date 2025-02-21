# StorageListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**token_id** | **str** |  | [optional] 
**token_secret** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.storage_list_command import StorageListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of StorageListCommand from a JSON string
storage_list_command_instance = StorageListCommand.from_json(json)
# print the JSON string representation of the object
print(StorageListCommand.to_json())

# convert the object into a dict
storage_list_command_dict = storage_list_command_instance.to_dict()
# create an instance of StorageListCommand from a dict
storage_list_command_from_dict = StorageListCommand.from_dict(storage_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


