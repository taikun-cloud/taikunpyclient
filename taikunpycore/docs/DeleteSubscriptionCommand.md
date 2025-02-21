# DeleteSubscriptionCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.delete_subscription_command import DeleteSubscriptionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSubscriptionCommand from a JSON string
delete_subscription_command_instance = DeleteSubscriptionCommand.from_json(json)
# print the JSON string representation of the object
print(DeleteSubscriptionCommand.to_json())

# convert the object into a dict
delete_subscription_command_dict = delete_subscription_command_instance.to_dict()
# create an instance of DeleteSubscriptionCommand from a dict
delete_subscription_command_from_dict = DeleteSubscriptionCommand.from_dict(delete_subscription_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


