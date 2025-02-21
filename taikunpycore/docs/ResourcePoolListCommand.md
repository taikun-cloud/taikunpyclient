# ResourcePoolListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**datacenter_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.resource_pool_list_command import ResourcePoolListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePoolListCommand from a JSON string
resource_pool_list_command_instance = ResourcePoolListCommand.from_json(json)
# print the JSON string representation of the object
print(ResourcePoolListCommand.to_json())

# convert the object into a dict
resource_pool_list_command_dict = resource_pool_list_command_instance.to_dict()
# create an instance of ResourcePoolListCommand from a dict
resource_pool_list_command_from_dict = ResourcePoolListCommand.from_dict(resource_pool_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


