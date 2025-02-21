# AzureSubscriptionListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.azure_subscription_list_command import AzureSubscriptionListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSubscriptionListCommand from a JSON string
azure_subscription_list_command_instance = AzureSubscriptionListCommand.from_json(json)
# print the JSON string representation of the object
print(AzureSubscriptionListCommand.to_json())

# convert the object into a dict
azure_subscription_list_command_dict = azure_subscription_list_command_instance.to_dict()
# create an instance of AzureSubscriptionListCommand from a dict
azure_subscription_list_command_from_dict = AzureSubscriptionListCommand.from_dict(azure_subscription_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


