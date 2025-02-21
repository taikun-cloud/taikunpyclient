# ArtifactUrlCheckerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.artifact_url_checker_command import ArtifactUrlCheckerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactUrlCheckerCommand from a JSON string
artifact_url_checker_command_instance = ArtifactUrlCheckerCommand.from_json(json)
# print the JSON string representation of the object
print(ArtifactUrlCheckerCommand.to_json())

# convert the object into a dict
artifact_url_checker_command_dict = artifact_url_checker_command_instance.to_dict()
# create an instance of ArtifactUrlCheckerCommand from a dict
artifact_url_checker_command_from_dict = ArtifactUrlCheckerCommand.from_dict(artifact_url_checker_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


