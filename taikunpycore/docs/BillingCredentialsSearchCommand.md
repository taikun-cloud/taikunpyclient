# BillingCredentialsSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.billing_credentials_search_command import BillingCredentialsSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of BillingCredentialsSearchCommand from a JSON string
billing_credentials_search_command_instance = BillingCredentialsSearchCommand.from_json(json)
# print the JSON string representation of the object
print(BillingCredentialsSearchCommand.to_json())

# convert the object into a dict
billing_credentials_search_command_dict = billing_credentials_search_command_instance.to_dict()
# create an instance of BillingCredentialsSearchCommand from a dict
billing_credentials_search_command_from_dict = BillingCredentialsSearchCommand.from_dict(billing_credentials_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


