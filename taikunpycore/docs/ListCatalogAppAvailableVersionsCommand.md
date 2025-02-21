# ListCatalogAppAvailableVersionsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo_name** | **str** |  | [optional] 
**package_name** | **str** |  | [optional] 
**current_version** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.list_catalog_app_available_versions_command import ListCatalogAppAvailableVersionsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ListCatalogAppAvailableVersionsCommand from a JSON string
list_catalog_app_available_versions_command_instance = ListCatalogAppAvailableVersionsCommand.from_json(json)
# print the JSON string representation of the object
print(ListCatalogAppAvailableVersionsCommand.to_json())

# convert the object into a dict
list_catalog_app_available_versions_command_dict = list_catalog_app_available_versions_command_instance.to_dict()
# create an instance of ListCatalogAppAvailableVersionsCommand from a dict
list_catalog_app_available_versions_command_from_dict = ListCatalogAppAvailableVersionsCommand.from_dict(list_catalog_app_available_versions_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


