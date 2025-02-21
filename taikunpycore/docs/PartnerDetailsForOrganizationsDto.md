# PartnerDetailsForOrganizationsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.partner_details_for_organizations_dto import PartnerDetailsForOrganizationsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerDetailsForOrganizationsDto from a JSON string
partner_details_for_organizations_dto_instance = PartnerDetailsForOrganizationsDto.from_json(json)
# print the JSON string representation of the object
print(PartnerDetailsForOrganizationsDto.to_json())

# convert the object into a dict
partner_details_for_organizations_dto_dict = partner_details_for_organizations_dto_instance.to_dict()
# create an instance of PartnerDetailsForOrganizationsDto from a dict
partner_details_for_organizations_dto_from_dict = PartnerDetailsForOrganizationsDto.from_dict(partner_details_for_organizations_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


