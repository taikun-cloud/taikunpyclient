# UpdateSubscriptionCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**project_limit** | **int** |  | [optional] 
**server_limit** | **int** |  | [optional] 
**user_limit** | **int** |  | [optional] 
**cloud_credential_limit** | **int** |  | [optional] 
**monthly_price** | **float** |  | [optional] 
**yearly_price** | **float** |  | [optional] 
**tcu_price** | **float** |  | [optional] 
**trial_days** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.update_subscription_command import UpdateSubscriptionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSubscriptionCommand from a JSON string
update_subscription_command_instance = UpdateSubscriptionCommand.from_json(json)
# print the JSON string representation of the object
print(UpdateSubscriptionCommand.to_json())

# convert the object into a dict
update_subscription_command_dict = update_subscription_command_instance.to_dict()
# create an instance of UpdateSubscriptionCommand from a dict
update_subscription_command_from_dict = UpdateSubscriptionCommand.from_dict(update_subscription_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


