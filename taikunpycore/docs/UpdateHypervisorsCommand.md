# UpdateHypervisorsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**hypervisors** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.update_hypervisors_command import UpdateHypervisorsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHypervisorsCommand from a JSON string
update_hypervisors_command_instance = UpdateHypervisorsCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateHypervisorsCommand.to_json())

# convert the object into a dict
update_hypervisors_command_dict = update_hypervisors_command_instance.to_dict()
# create an instance of UpdateHypervisorsCommand from a dict
update_hypervisors_command_from_dict = UpdateHypervisorsCommand.from_dict(update_hypervisors_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


