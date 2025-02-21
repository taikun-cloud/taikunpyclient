# InfraBillingListCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | [optional] 
**filter** | [**DateFilter**](DateFilter.md) |  | [optional] 

## Example

```python
from taikunpycore.models.infra_billing_list_command import InfraBillingListCommand

# TODO update the JSON string below
json = "{}"
# create an instance of InfraBillingListCommand from a JSON string
infra_billing_list_command_instance = InfraBillingListCommand.from_json(json)
# print the JSON string representation of the object
print(InfraBillingListCommand.to_json())

# convert the object into a dict
infra_billing_list_command_dict = infra_billing_list_command_instance.to_dict()
# create an instance of InfraBillingListCommand from a dict
infra_billing_list_command_from_dict = InfraBillingListCommand.from_dict(infra_billing_list_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


