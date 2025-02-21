# Metadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infracost_command** | **str** |  | [optional] 
**vcs_branch** | **str** |  | [optional] 
**vcs_commit_sha** | **str** |  | [optional] 
**vcs_commit_author_name** | **str** |  | [optional] 
**vcs_commit_author_email** | **str** |  | [optional] 
**vcs_commit_timestamp** | **str** |  | [optional] 
**vcs_commit_message** | **str** |  | [optional] 
**vcs_repository_url** | **str** |  | [optional] 
**usage_api_enabled** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.metadata import Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of Metadata from a JSON string
metadata_instance = Metadata.from_json(json)
# print the JSON string representation of the object
print(Metadata.to_json())

# convert the object into a dict
metadata_dict = metadata_instance.to_dict()
# create an instance of Metadata from a dict
metadata_from_dict = Metadata.from_dict(metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


