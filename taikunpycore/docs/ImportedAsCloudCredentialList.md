# ImportedAsCloudCredentialList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visibility** | [**ImportedAsCloudCredentialVisibility**](ImportedAsCloudCredentialVisibility.md) |  | 
**data** | [**ImportedClusterDetailsDto**](ImportedClusterDetailsDto.md) |  | 

## Example

```python
from taikunpycore.models.imported_as_cloud_credential_list import ImportedAsCloudCredentialList

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedAsCloudCredentialList from a JSON string
imported_as_cloud_credential_list_instance = ImportedAsCloudCredentialList.from_json(json)
# print the JSON string representation of the object
print(ImportedAsCloudCredentialList.to_json())

# convert the object into a dict
imported_as_cloud_credential_list_dict = imported_as_cloud_credential_list_instance.to_dict()
# create an instance of ImportedAsCloudCredentialList from a dict
imported_as_cloud_credential_list_from_dict = ImportedAsCloudCredentialList.from_dict(imported_as_cloud_credential_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


