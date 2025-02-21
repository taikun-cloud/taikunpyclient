# UpdateAwsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**aws_secret_access_key** | **str** |  | [optional] 
**aws_access_key_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_aws_command import UpdateAwsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAwsCommand from a JSON string
update_aws_command_instance = UpdateAwsCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateAwsCommand.to_json())

# convert the object into a dict
update_aws_command_dict = update_aws_command_instance.to_dict()
# create an instance of UpdateAwsCommand from a dict
update_aws_command_from_dict = UpdateAwsCommand.from_dict(update_aws_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


