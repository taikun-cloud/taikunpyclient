# CreateAiCredentialCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**api_key** | **str** |  | [optional] 
**organization_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.create_ai_credential_command import CreateAiCredentialCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAiCredentialCommand from a JSON string
create_ai_credential_command_instance = CreateAiCredentialCommand.from_json(json)
# print the JSON string representation of the object
print(CreateAiCredentialCommand.to_json())

# convert the object into a dict
create_ai_credential_command_dict = create_ai_credential_command_instance.to_dict()
# create an instance of CreateAiCredentialCommand from a dict
create_ai_credential_command_from_dict = CreateAiCredentialCommand.from_dict(create_ai_credential_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


