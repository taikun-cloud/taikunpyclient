# OrganizationSubscriptionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**organization_id** | **int** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**subscription_id** | **int** |  | [optional] 
**stripe_subscription_id** | **str** |  | [optional] 
**subscription_type** | **str** |  | [optional] 
**subscription_name** | **str** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**invoices** | [**List[InvoiceDto]**](InvoiceDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.organization_subscription_dto import OrganizationSubscriptionDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSubscriptionDto from a JSON string
organization_subscription_dto_instance = OrganizationSubscriptionDto.from_json(json)
# print the JSON string representation of the object
print(OrganizationSubscriptionDto.to_json())

# convert the object into a dict
organization_subscription_dto_dict = organization_subscription_dto_instance.to_dict()
# create an instance of OrganizationSubscriptionDto from a dict
organization_subscription_dto_from_dict = OrganizationSubscriptionDto.from_dict(organization_subscription_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


