# CheckS3Command


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_access_key_id** | **str** |  | [optional] 
**s3_secret_key** | **str** |  | [optional] 
**s3_endpoint** | **str** |  | [optional] 
**s3_region** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.check_s3_command import CheckS3Command

# TODO update the JSON string below
json = "{}"
# create an instance of CheckS3Command from a JSON string
check_s3_command_instance = CheckS3Command.from_json(json)
# print the JSON string representation of the object
print(CheckS3Command.to_json())

# convert the object into a dict
check_s3_command_dict = check_s3_command_instance.to_dict()
# create an instance of CheckS3Command from a dict
check_s3_command_from_dict = CheckS3Command.from_dict(check_s3_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


