# PrometheusBillingCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**prometheus_rule_id** | **int** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**price** | **float** |  | [optional] 

## Example

```python
from taikunpycore.models.prometheus_billing_create_command import PrometheusBillingCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of PrometheusBillingCreateCommand from a JSON string
prometheus_billing_create_command_instance = PrometheusBillingCreateCommand.from_json(json)
# print the JSON string representation of the object
print(PrometheusBillingCreateCommand.to_json())

# convert the object into a dict
prometheus_billing_create_command_dict = prometheus_billing_create_command_instance.to_dict()
# create an instance of PrometheusBillingCreateCommand from a dict
prometheus_billing_create_command_from_dict = PrometheusBillingCreateCommand.from_dict(prometheus_billing_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


