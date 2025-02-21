# RestartStsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.restart_sts_command import RestartStsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of RestartStsCommand from a JSON string
restart_sts_command_instance = RestartStsCommand.from_json(json)
# print the JSON string representation of the object
print(RestartStsCommand.to_json())

# convert the object into a dict
restart_sts_command_dict = restart_sts_command_instance.to_dict()
# create an instance of RestartStsCommand from a dict
restart_sts_command_from_dict = RestartStsCommand.from_dict(restart_sts_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


