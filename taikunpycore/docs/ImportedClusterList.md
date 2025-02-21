# ImportedClusterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ImportedClusterListDto]**](ImportedClusterListDto.md) |  | 
**project** | [**ImportedClusterDetailsDto**](ImportedClusterDetailsDto.md) |  | 

## Example

```python
from taikunpycore.models.imported_cluster_list import ImportedClusterList

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedClusterList from a JSON string
imported_cluster_list_instance = ImportedClusterList.from_json(json)
# print the JSON string representation of the object
print(ImportedClusterList.to_json())

# convert the object into a dict
imported_cluster_list_dict = imported_cluster_list_instance.to_dict()
# create an instance of ImportedClusterList from a dict
imported_cluster_list_from_dict = ImportedClusterList.from_dict(imported_cluster_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


