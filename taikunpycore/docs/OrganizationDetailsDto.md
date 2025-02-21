# OrganizationDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**is_eligible_update_subscription** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**is_read_only** | **bool** |  | [optional] 
**is_new** | **bool** |  | [optional] 
**trial_ended** | **bool** |  | [optional] 
**users** | **int** |  | [optional] 
**projects** | **int** |  | [optional] 
**servers** | **int** |  | [optional] 
**cloud_credentials** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**partner_id** | **int** |  | [optional] 
**partner_name** | **str** |  | [optional] 
**partner** | [**PartnerDetailsForOrganizationsDto**](PartnerDetailsForOrganizationsDto.md) |  | [optional] 
**discount_rate** | **float** |  | [optional] 
**bound_rules** | [**List[PrometheusEntity]**](PrometheusEntity.md) |  | [optional] 

## Example

```python
from taikunpycore.models.organization_details_dto import OrganizationDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationDetailsDto from a JSON string
organization_details_dto_instance = OrganizationDetailsDto.from_json(json)
# print the JSON string representation of the object
print(OrganizationDetailsDto.to_json())

# convert the object into a dict
organization_details_dto_dict = organization_details_dto_instance.to_dict()
# create an instance of OrganizationDetailsDto from a dict
organization_details_dto_from_dict = OrganizationDetailsDto.from_dict(organization_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


