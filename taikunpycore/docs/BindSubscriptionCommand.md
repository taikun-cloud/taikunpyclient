# BindSubscriptionCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**yearly** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.bind_subscription_command import BindSubscriptionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BindSubscriptionCommand from a JSON string
bind_subscription_command_instance = BindSubscriptionCommand.from_json(json)
# print the JSON string representation of the object
print(BindSubscriptionCommand.to_json())

# convert the object into a dict
bind_subscription_command_dict = bind_subscription_command_instance.to_dict()
# create an instance of BindSubscriptionCommand from a dict
bind_subscription_command_from_dict = BindSubscriptionCommand.from_dict(bind_subscription_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


