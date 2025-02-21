# UpdateTanzuCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_tanzu_command import UpdateTanzuCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTanzuCommand from a JSON string
update_tanzu_command_instance = UpdateTanzuCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateTanzuCommand.to_json())

# convert the object into a dict
update_tanzu_command_dict = update_tanzu_command_instance.to_dict()
# create an instance of UpdateTanzuCommand from a dict
update_tanzu_command_from_dict = UpdateTanzuCommand.from_dict(update_tanzu_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


