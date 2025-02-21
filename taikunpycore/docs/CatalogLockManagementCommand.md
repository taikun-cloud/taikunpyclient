# CatalogLockManagementCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.catalog_lock_management_command import CatalogLockManagementCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogLockManagementCommand from a JSON string
catalog_lock_management_command_instance = CatalogLockManagementCommand.from_json(json)
# print the JSON string representation of the object
print(CatalogLockManagementCommand.to_json())

# convert the object into a dict
catalog_lock_management_command_dict = catalog_lock_management_command_instance.to_dict()
# create an instance of CatalogLockManagementCommand from a dict
catalog_lock_management_command_from_dict = CatalogLockManagementCommand.from_dict(catalog_lock_management_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


