# UpdatePaymentIdCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **str** |  | [optional] 
**payment_intent_id** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.update_payment_id_command import UpdatePaymentIdCommand

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePaymentIdCommand from a JSON string
update_payment_id_command_instance = UpdatePaymentIdCommand.from_json(json)
# print the JSON string representation of the object
print(UpdatePaymentIdCommand.to_json())

# convert the object into a dict
update_payment_id_command_dict = update_payment_id_command_instance.to_dict()
# create an instance of UpdatePaymentIdCommand from a dict
update_payment_id_command_from_dict = UpdatePaymentIdCommand.from_dict(update_payment_id_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


