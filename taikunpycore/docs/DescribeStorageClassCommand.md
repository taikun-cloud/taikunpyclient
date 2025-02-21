# DescribeStorageClassCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_storage_class_command import DescribeStorageClassCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeStorageClassCommand from a JSON string
describe_storage_class_command_instance = DescribeStorageClassCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeStorageClassCommand.to_json())

# convert the object into a dict
describe_storage_class_command_dict = describe_storage_class_command_instance.to_dict()
# create an instance of DescribeStorageClassCommand from a dict
describe_storage_class_command_from_dict = DescribeStorageClassCommand.from_dict(describe_storage_class_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


