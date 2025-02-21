# ZededaCheckerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.zededa_checker_command import ZededaCheckerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ZededaCheckerCommand from a JSON string
zededa_checker_command_instance = ZededaCheckerCommand.from_json(json)
# print the JSON string representation of the object
print(ZededaCheckerCommand.to_json())

# convert the object into a dict
zededa_checker_command_dict = zededa_checker_command_instance.to_dict()
# create an instance of ZededaCheckerCommand from a dict
zededa_checker_command_from_dict = ZededaCheckerCommand.from_dict(zededa_checker_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


