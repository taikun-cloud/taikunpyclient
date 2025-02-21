# CreateCatalogCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_catalog_command import CreateCatalogCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCatalogCommand from a JSON string
create_catalog_command_instance = CreateCatalogCommand.from_json(json)
# print the JSON string representation of the object
print(CreateCatalogCommand.to_json())

# convert the object into a dict
create_catalog_command_dict = create_catalog_command_instance.to_dict()
# create an instance of CreateCatalogCommand from a dict
create_catalog_command_from_dict = CreateCatalogCommand.from_dict(create_catalog_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


