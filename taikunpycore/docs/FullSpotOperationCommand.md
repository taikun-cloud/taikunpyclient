# FullSpotOperationCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.full_spot_operation_command import FullSpotOperationCommand

# TODO update the JSON string below
json = "{}"
# create an instance of FullSpotOperationCommand from a JSON string
full_spot_operation_command_instance = FullSpotOperationCommand.from_json(json)
# print the JSON string representation of the object
print(FullSpotOperationCommand.to_json())

# convert the object into a dict
full_spot_operation_command_dict = full_spot_operation_command_instance.to_dict()
# create an instance of FullSpotOperationCommand from a dict
full_spot_operation_command_from_dict = FullSpotOperationCommand.from_dict(full_spot_operation_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


