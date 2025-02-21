# ZededaProjectsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_url** | **str** |  | [optional] 
**api_token** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.zededa_projects_command import ZededaProjectsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ZededaProjectsCommand from a JSON string
zededa_projects_command_instance = ZededaProjectsCommand.from_json(json)
# print the JSON string representation of the object
print(ZededaProjectsCommand.to_json())

# convert the object into a dict
zededa_projects_command_dict = zededa_projects_command_instance.to_dict()
# create an instance of ZededaProjectsCommand from a dict
zededa_projects_command_from_dict = ZededaProjectsCommand.from_dict(zededa_projects_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


