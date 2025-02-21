# ImportedAsFullyManagedList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visibility** | [**ImportedAsFullyManagedVisibility**](ImportedAsFullyManagedVisibility.md) |  | 
**data** | [**ImportedClusterDetailsDto**](ImportedClusterDetailsDto.md) |  | 

## Example

```python
from taikunpycore.models.imported_as_fully_managed_list import ImportedAsFullyManagedList

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedAsFullyManagedList from a JSON string
imported_as_fully_managed_list_instance = ImportedAsFullyManagedList.from_json(json)
# print the JSON string representation of the object
print(ImportedAsFullyManagedList.to_json())

# convert the object into a dict
imported_as_fully_managed_list_dict = imported_as_fully_managed_list_instance.to_dict()
# create an instance of ImportedAsFullyManagedList from a dict
imported_as_fully_managed_list_from_dict = ImportedAsFullyManagedList.from_dict(imported_as_fully_managed_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


