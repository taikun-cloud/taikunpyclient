# EditCatalogAppParamCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog_app_id** | **int** |  | [optional] 
**parameters** | [**List[CatalogAppParamsDto]**](CatalogAppParamsDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.edit_catalog_app_param_command import EditCatalogAppParamCommand

# TODO update the JSON string below
json = "{}"
# create an instance of EditCatalogAppParamCommand from a JSON string
edit_catalog_app_param_command_instance = EditCatalogAppParamCommand.from_json(json)
# print the JSON string representation of the object
print(EditCatalogAppParamCommand.to_json())

# convert the object into a dict
edit_catalog_app_param_command_dict = edit_catalog_app_param_command_instance.to_dict()
# create an instance of EditCatalogAppParamCommand from a dict
edit_catalog_app_param_command_from_dict = EditCatalogAppParamCommand.from_dict(edit_catalog_app_param_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


