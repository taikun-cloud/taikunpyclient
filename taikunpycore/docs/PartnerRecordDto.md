# PartnerRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**logo_url** | **str** |  | 
**background_image_url** | **str** |  | 
**payment_enabled** | **bool** |  | 
**allow_registration** | **bool** |  | 
**partner_color_settings** | [**PartnerColorSettingsDto**](PartnerColorSettingsDto.md) |  | [optional] 
**partner_image_settings** | [**PartnerImageSettingsDto**](PartnerImageSettingsDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.partner_record_dto import PartnerRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerRecordDto from a JSON string
partner_record_dto_instance = PartnerRecordDto.from_json(json)
# print the JSON string representation of the object
print(PartnerRecordDto.to_json())

# convert the object into a dict
partner_record_dto_dict = partner_record_dto_instance.to_dict()
# create an instance of PartnerRecordDto from a dict
partner_record_dto_from_dict = PartnerRecordDto.from_dict(partner_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


