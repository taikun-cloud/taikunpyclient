# CheckZadaraCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zadara_secret_access_key** | **str** |  | [optional] 
**zadara_access_key_id** | **str** |  | [optional] 
**zadara_url** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.check_zadara_command import CheckZadaraCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CheckZadaraCommand from a JSON string
check_zadara_command_instance = CheckZadaraCommand.from_json(json)
# print the JSON string representation of the object
print(CheckZadaraCommand.to_json())

# convert the object into a dict
check_zadara_command_dict = check_zadara_command_instance.to_dict()
# create an instance of CheckZadaraCommand from a dict
check_zadara_command_from_dict = CheckZadaraCommand.from_dict(check_zadara_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


