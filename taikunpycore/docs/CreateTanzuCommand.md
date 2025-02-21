# CreateTanzuCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**volume_type** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**tanzu_continent** | **str** |  | [optional] 
**port** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_tanzu_command import CreateTanzuCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTanzuCommand from a JSON string
create_tanzu_command_instance = CreateTanzuCommand.from_json(json)
# print the JSON string representation of the object
print(CreateTanzuCommand.to_json())

# convert the object into a dict
create_tanzu_command_dict = create_tanzu_command_instance.to_dict()
# create an instance of CreateTanzuCommand from a dict
create_tanzu_command_from_dict = CreateTanzuCommand.from_dict(create_tanzu_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


