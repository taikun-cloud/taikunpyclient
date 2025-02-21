# UpdateOrganizationSubscriptionCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **int** |  | [optional] 
**is_yearly** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.update_organization_subscription_command import UpdateOrganizationSubscriptionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationSubscriptionCommand from a JSON string
update_organization_subscription_command_instance = UpdateOrganizationSubscriptionCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationSubscriptionCommand.to_json())

# convert the object into a dict
update_organization_subscription_command_dict = update_organization_subscription_command_instance.to_dict()
# create an instance of UpdateOrganizationSubscriptionCommand from a dict
update_organization_subscription_command_from_dict = UpdateOrganizationSubscriptionCommand.from_dict(update_organization_subscription_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


