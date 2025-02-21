# DescribeSecretCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.describe_secret_command import DescribeSecretCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DescribeSecretCommand from a JSON string
describe_secret_command_instance = DescribeSecretCommand.from_json(json)
# print the JSON string representation of the object
print(DescribeSecretCommand.to_json())

# convert the object into a dict
describe_secret_command_dict = describe_secret_command_instance.to_dict()
# create an instance of DescribeSecretCommand from a dict
describe_secret_command_from_dict = DescribeSecretCommand.from_dict(describe_secret_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


