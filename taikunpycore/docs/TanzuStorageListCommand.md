# TanzuStorageListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**port** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.tanzu_storage_list_command import TanzuStorageListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of TanzuStorageListCommand from a JSON string
tanzu_storage_list_command_instance = TanzuStorageListCommand.from_json(json)
# print the JSON string representation of the object
print(TanzuStorageListCommand.to_json())

# convert the object into a dict
tanzu_storage_list_command_dict = tanzu_storage_list_command_instance.to_dict()
# create an instance of TanzuStorageListCommand from a dict
tanzu_storage_list_command_from_dict = TanzuStorageListCommand.from_dict(tanzu_storage_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


