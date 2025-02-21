# VerifyWebhookCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.verify_webhook_command import VerifyWebhookCommand

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebhookCommand from a JSON string
verify_webhook_command_instance = VerifyWebhookCommand.from_json(json)
# print the JSON string representation of the object
print(VerifyWebhookCommand.to_json())

# convert the object into a dict
verify_webhook_command_dict = verify_webhook_command_instance.to_dict()
# create an instance of VerifyWebhookCommand from a dict
verify_webhook_command_from_dict = VerifyWebhookCommand.from_dict(verify_webhook_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


