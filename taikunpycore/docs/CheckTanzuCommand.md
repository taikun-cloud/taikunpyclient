# CheckTanzuCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**volume_type** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.check_tanzu_command import CheckTanzuCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CheckTanzuCommand from a JSON string
check_tanzu_command_instance = CheckTanzuCommand.from_json(json)
# print the JSON string representation of the object
print(CheckTanzuCommand.to_json())

# convert the object into a dict
check_tanzu_command_dict = check_tanzu_command_instance.to_dict()
# create an instance of CheckTanzuCommand from a dict
check_tanzu_command_from_dict = CheckTanzuCommand.from_dict(check_tanzu_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


