# EditArticleCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | [optional] 
**body** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.edit_article_command import EditArticleCommand

# TODO update the JSON string below
json = "{}"
# create an instance of EditArticleCommand from a JSON string
edit_article_command_instance = EditArticleCommand.from_json(json)
# print the JSON string representation of the object
print(EditArticleCommand.to_json())

# convert the object into a dict
edit_article_command_dict = edit_article_command_instance.to_dict()
# create an instance of EditArticleCommand from a dict
edit_article_command_from_dict = EditArticleCommand.from_dict(edit_article_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


