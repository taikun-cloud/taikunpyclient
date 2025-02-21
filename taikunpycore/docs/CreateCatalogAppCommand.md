# CreateCatalogAppCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repo_name** | **str** |  | [optional] 
**package_name** | **str** |  | [optional] 
**catalog_id** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**parameters** | [**List[CatalogAppParamsDto]**](CatalogAppParamsDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.create_catalog_app_command import CreateCatalogAppCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCatalogAppCommand from a JSON string
create_catalog_app_command_instance = CreateCatalogAppCommand.from_json(json)
# print the JSON string representation of the object
print(CreateCatalogAppCommand.to_json())

# convert the object into a dict
create_catalog_app_command_dict = create_catalog_app_command_instance.to_dict()
# create an instance of CreateCatalogAppCommand from a dict
create_catalog_app_command_from_dict = CreateCatalogAppCommand.from_dict(create_catalog_app_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


