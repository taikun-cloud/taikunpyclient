# ArtifactRepositoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_id** | **str** |  | 
**app_repo_id** | **int** |  | 
**name** | **str** |  | 
**display_name** | **str** |  | 
**url** | **str** |  | 
**organization_name** | **str** |  | 
**disabled** | **bool** |  | 
**verified_publisher** | **bool** |  | 
**official** | **bool** |  | 
**is_bound** | **bool** |  | 
**is_private** | **bool** |  | [optional] 
**is_taikun** | **bool** |  | 
**has_catalog_app** | **bool** |  | 

## Example

```python
from taikunpycore.models.artifact_repository_dto import ArtifactRepositoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactRepositoryDto from a JSON string
artifact_repository_dto_instance = ArtifactRepositoryDto.from_json(json)
# print the JSON string representation of the object
print(ArtifactRepositoryDto.to_json())

# convert the object into a dict
artifact_repository_dto_dict = artifact_repository_dto_instance.to_dict()
# create an instance of ArtifactRepositoryDto from a dict
artifact_repository_dto_from_dict = ArtifactRepositoryDto.from_dict(artifact_repository_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


