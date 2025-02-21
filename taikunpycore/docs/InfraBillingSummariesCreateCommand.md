# InfraBillingSummariesCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**begin_apply** | **datetime** |  | [optional] 
**end_apply** | **datetime** |  | [optional] 
**product_id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.infra_billing_summaries_create_command import InfraBillingSummariesCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of InfraBillingSummariesCreateCommand from a JSON string
infra_billing_summaries_create_command_instance = InfraBillingSummariesCreateCommand.from_json(json)
# print the JSON string representation of the object
print(InfraBillingSummariesCreateCommand.to_json())

# convert the object into a dict
infra_billing_summaries_create_command_dict = infra_billing_summaries_create_command_instance.to_dict()
# create an instance of InfraBillingSummariesCreateCommand from a dict
infra_billing_summaries_create_command_from_dict = InfraBillingSummariesCreateCommand.from_dict(infra_billing_summaries_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


