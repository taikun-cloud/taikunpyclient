# GetCatalogAppValueCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.get_catalog_app_value_command import GetCatalogAppValueCommand

# TODO update the JSON string below
json = "{}"
# create an instance of GetCatalogAppValueCommand from a JSON string
get_catalog_app_value_command_instance = GetCatalogAppValueCommand.from_json(json)
# print the JSON string representation of the object
print(GetCatalogAppValueCommand.to_json())

# convert the object into a dict
get_catalog_app_value_command_dict = get_catalog_app_value_command_instance.to_dict()
# create an instance of GetCatalogAppValueCommand from a dict
get_catalog_app_value_command_from_dict = GetCatalogAppValueCommand.from_dict(get_catalog_app_value_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


