# ImageByIdCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_id** | **int** |  | [optional] 
**image_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.image_by_id_command import ImageByIdCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ImageByIdCommand from a JSON string
image_by_id_command_instance = ImageByIdCommand.from_json(json)
# print the JSON string representation of the object
print(ImageByIdCommand.to_json())

# convert the object into a dict
image_by_id_command_dict = image_by_id_command_instance.to_dict()
# create an instance of ImageByIdCommand from a dict
image_by_id_command_from_dict = ImageByIdCommand.from_dict(image_by_id_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


