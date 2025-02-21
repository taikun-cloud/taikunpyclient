# AwsImagesPostListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_id** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**sort_by** | **str** |  | [optional] 
**sort_direction** | **str** |  | [optional] 
**search** | **str** |  | [optional] 
**latest** | **bool** |  | [optional] 
**owners** | **List[str]** |  | [optional] 
**project_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.aws_images_post_list_command import AwsImagesPostListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AwsImagesPostListCommand from a JSON string
aws_images_post_list_command_instance = AwsImagesPostListCommand.from_json(json)
# print the JSON string representation of the object
print(AwsImagesPostListCommand.to_json())

# convert the object into a dict
aws_images_post_list_command_dict = aws_images_post_list_command_instance.to_dict()
# create an instance of AwsImagesPostListCommand from a dict
aws_images_post_list_command_from_dict = AwsImagesPostListCommand.from_dict(aws_images_post_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


