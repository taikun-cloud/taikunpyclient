# GetCatalogAppValueAutocompleteCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**catalog_app_id** | **int** |  | [optional] 
**is_question** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.get_catalog_app_value_autocomplete_command import GetCatalogAppValueAutocompleteCommand

# TODO update the JSON string below
json = "{}"
# create an instance of GetCatalogAppValueAutocompleteCommand from a JSON string
get_catalog_app_value_autocomplete_command_instance = GetCatalogAppValueAutocompleteCommand.from_json(json)
# print the JSON string representation of the object
print(GetCatalogAppValueAutocompleteCommand.to_json())

# convert the object into a dict
get_catalog_app_value_autocomplete_command_dict = get_catalog_app_value_autocomplete_command_instance.to_dict()
# create an instance of GetCatalogAppValueAutocompleteCommand from a dict
get_catalog_app_value_autocomplete_command_from_dict = GetCatalogAppValueAutocompleteCommand.from_dict(get_catalog_app_value_autocomplete_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


