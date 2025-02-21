# ImportedAsReadOnlyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visibility** | [**ImportedAsReadOnlyVisibility**](ImportedAsReadOnlyVisibility.md) |  | 
**data** | [**ImportedClusterDetailsDto**](ImportedClusterDetailsDto.md) |  | 

## Example

```python
from taikunpycore.models.imported_as_read_only_list import ImportedAsReadOnlyList

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedAsReadOnlyList from a JSON string
imported_as_read_only_list_instance = ImportedAsReadOnlyList.from_json(json)
# print the JSON string representation of the object
print(ImportedAsReadOnlyList.to_json())

# convert the object into a dict
imported_as_read_only_list_dict = imported_as_read_only_list_instance.to_dict()
# create an instance of ImportedAsReadOnlyList from a dict
imported_as_read_only_list_from_dict = ImportedAsReadOnlyList.from_dict(imported_as_read_only_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


