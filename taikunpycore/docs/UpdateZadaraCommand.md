# UpdateZadaraCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**zadara_secret_access_key** | **str** |  | [optional] 
**zadara_access_key_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_zadara_command import UpdateZadaraCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateZadaraCommand from a JSON string
update_zadara_command_instance = UpdateZadaraCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateZadaraCommand.to_json())

# convert the object into a dict
update_zadara_command_dict = update_zadara_command_instance.to_dict()
# create an instance of UpdateZadaraCommand from a dict
update_zadara_command_from_dict = UpdateZadaraCommand.from_dict(update_zadara_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


