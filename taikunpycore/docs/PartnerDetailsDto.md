# PartnerDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**link** | **str** |  | 
**domain** | **str** |  | 
**country** | **str** |  | 
**city** | **str** |  | 
**vat_number** | **str** |  | 
**background_image_url** | **str** |  | 
**address** | **str** |  | 
**logo** | **str** |  | 
**phone** | **str** |  | 
**email** | **str** |  | 
**payment_enabled** | **bool** |  | 
**allow_registration** | **bool** |  | 
**required_user_approval** | **bool** |  | 
**organizations** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**white_list_domains** | [**List[WhiteListDomainDto]**](WhiteListDomainDto.md) |  | 
**partner_color_settings** | [**PartnerColorSettingsDto**](PartnerColorSettingsDto.md) |  | [optional] 
**partner_image_settings** | [**PartnerImageSettingsDto**](PartnerImageSettingsDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.partner_details_dto import PartnerDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerDetailsDto from a JSON string
partner_details_dto_instance = PartnerDetailsDto.from_json(json)
# print the JSON string representation of the object
print(PartnerDetailsDto.to_json())

# convert the object into a dict
partner_details_dto_dict = partner_details_dto_instance.to_dict()
# create an instance of PartnerDetailsDto from a dict
partner_details_dto_from_dict = PartnerDetailsDto.from_dict(partner_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


