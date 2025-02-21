# CreateExecutorCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**local_cluster** | **bool** |  | [optional] 
**continent** | **str** |  | [optional] 
**kube_config** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.create_executor_command import CreateExecutorCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExecutorCommand from a JSON string
create_executor_command_instance = CreateExecutorCommand.from_json(json)
# print the JSON string representation of the object
print(CreateExecutorCommand.to_json())

# convert the object into a dict
create_executor_command_dict = create_executor_command_instance.to_dict()
# create an instance of CreateExecutorCommand from a dict
create_executor_command_from_dict = CreateExecutorCommand.from_dict(create_executor_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


