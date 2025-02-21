# ChatCompletionsCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | **object** |  | [optional] 

## Example

```python
from taikunpycore.models.chat_completions_command import ChatCompletionsCommand

# TODO update the JSON string below
json = "{}"
# create an instance of ChatCompletionsCommand from a JSON string
chat_completions_command_instance = ChatCompletionsCommand.from_json(json)
# print the JSON string representation of the object
print(ChatCompletionsCommand.to_json())

# convert the object into a dict
chat_completions_command_dict = chat_completions_command_instance.to_dict()
# create an instance of ChatCompletionsCommand from a dict
chat_completions_command_from_dict = ChatCompletionsCommand.from_dict(chat_completions_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


