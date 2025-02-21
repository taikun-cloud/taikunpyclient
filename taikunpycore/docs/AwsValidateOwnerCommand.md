# AwsValidateOwnerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_id** | **int** |  | [optional] 
**owners** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.aws_validate_owner_command import AwsValidateOwnerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AwsValidateOwnerCommand from a JSON string
aws_validate_owner_command_instance = AwsValidateOwnerCommand.from_json(json)
# print the JSON string representation of the object
print(AwsValidateOwnerCommand.to_json())

# convert the object into a dict
aws_validate_owner_command_dict = aws_validate_owner_command_instance.to_dict()
# create an instance of AwsValidateOwnerCommand from a dict
aws_validate_owner_command_from_dict = AwsValidateOwnerCommand.from_dict(aws_validate_owner_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


