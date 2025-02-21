# EditCatalogAppVersionCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_app_id** | **int** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.edit_catalog_app_version_command import EditCatalogAppVersionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of EditCatalogAppVersionCommand from a JSON string
edit_catalog_app_version_command_instance = EditCatalogAppVersionCommand.from_json(json)
# print the JSON string representation of the object
print(EditCatalogAppVersionCommand.to_json())

# convert the object into a dict
edit_catalog_app_version_command_dict = edit_catalog_app_version_command_instance.to_dict()
# create an instance of EditCatalogAppVersionCommand from a dict
edit_catalog_app_version_command_from_dict = EditCatalogAppVersionCommand.from_dict(edit_catalog_app_version_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


