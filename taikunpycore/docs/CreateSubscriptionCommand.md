# CreateSubscriptionCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**project_limit** | **int** |  | [optional] 
**server_limit** | **int** |  | [optional] 
**user_limit** | **int** |  | [optional] 
**cloud_credential_limit** | **int** |  | [optional] 
**trial_days** | **int** |  | [optional] 
**monthly_price** | **float** |  | [optional] 
**tcu_price** | **float** |  | [optional] 
**yearly_price** | **float** |  | [optional] 

## Example

```python
from taikunpycore.models.create_subscription_command import CreateSubscriptionCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionCommand from a JSON string
create_subscription_command_instance = CreateSubscriptionCommand.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionCommand.to_json())

# convert the object into a dict
create_subscription_command_dict = create_subscription_command_instance.to_dict()
# create an instance of CreateSubscriptionCommand from a dict
create_subscription_command_from_dict = CreateSubscriptionCommand.from_dict(create_subscription_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


