# CreateAwsCloudCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**aws_secret_access_key** | **str** |  | [optional] 
**aws_access_key_id** | **str** |  | [optional] 
**az_count** | **int** |  | [optional] 
**aws_region** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_aws_cloud_command import CreateAwsCloudCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAwsCloudCommand from a JSON string
create_aws_cloud_command_instance = CreateAwsCloudCommand.from_json(json)
# print the JSON string representation of the object
print(CreateAwsCloudCommand.to_json())

# convert the object into a dict
create_aws_cloud_command_dict = create_aws_cloud_command_instance.to_dict()
# create an instance of CreateAwsCloudCommand from a dict
create_aws_cloud_command_from_dict = CreateAwsCloudCommand.from_dict(create_aws_cloud_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


