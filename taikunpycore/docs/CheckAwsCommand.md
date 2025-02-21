# CheckAwsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_access_key_id** | **str** |  | [optional] 
**aws_secret_access_key** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.check_aws_command import CheckAwsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CheckAwsCommand from a JSON string
check_aws_command_instance = CheckAwsCommand.from_json(json)
# print the JSON string representation of the object
print(CheckAwsCommand.to_json())

# convert the object into a dict
check_aws_command_dict = check_aws_command_instance.to_dict()
# create an instance of CheckAwsCommand from a dict
check_aws_command_from_dict = CheckAwsCommand.from_dict(check_aws_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


