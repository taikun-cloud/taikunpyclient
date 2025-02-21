# ImportedAsCloudCredentialVisibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lock** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**unlock** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 
**add_v_cluster** | [**ButtonStatusDto**](ButtonStatusDto.md) |  | 

## Example

```python
from taikunpycore.models.imported_as_cloud_credential_visibility import ImportedAsCloudCredentialVisibility

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedAsCloudCredentialVisibility from a JSON string
imported_as_cloud_credential_visibility_instance = ImportedAsCloudCredentialVisibility.from_json(json)
# print the JSON string representation of the object
print(ImportedAsCloudCredentialVisibility.to_json())

# convert the object into a dict
imported_as_cloud_credential_visibility_dict = imported_as_cloud_credential_visibility_instance.to_dict()
# create an instance of ImportedAsCloudCredentialVisibility from a dict
imported_as_cloud_credential_visibility_from_dict = ImportedAsCloudCredentialVisibility.from_dict(imported_as_cloud_credential_visibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


