# CreateStripeCustomerCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.create_stripe_customer_command import CreateStripeCustomerCommand

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStripeCustomerCommand from a JSON string
create_stripe_customer_command_instance = CreateStripeCustomerCommand.from_json(json)
# print the JSON string representation of the object
print(CreateStripeCustomerCommand.to_json())

# convert the object into a dict
create_stripe_customer_command_dict = create_stripe_customer_command_instance.to_dict()
# create an instance of CreateStripeCustomerCommand from a dict
create_stripe_customer_command_from_dict = CreateStripeCustomerCommand.from_dict(create_stripe_customer_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


