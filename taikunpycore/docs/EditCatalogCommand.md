# EditCatalogCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.edit_catalog_command import EditCatalogCommand

# TODO update the JSON string below
json = "{}"
# create an instance of EditCatalogCommand from a JSON string
edit_catalog_command_instance = EditCatalogCommand.from_json(json)
# print the JSON string representation of the object
print(EditCatalogCommand.to_json())

# convert the object into a dict
edit_catalog_command_dict = edit_catalog_command_instance.to_dict()
# create an instance of EditCatalogCommand from a dict
edit_catalog_command_from_dict = EditCatalogCommand.from_dict(edit_catalog_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


