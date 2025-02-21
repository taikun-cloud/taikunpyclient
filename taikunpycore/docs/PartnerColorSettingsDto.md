# PartnerColorSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bg** | **str** |  | 
**bg_collapsed_sub_item** | **str** |  | 
**item_text** | **str** |  | 
**item_bg** | **str** |  | 
**item_bg_hover** | **str** |  | 
**item_text_active** | **str** |  | 
**item_bg_active** | **str** |  | 
**item_bg_active_hover** | **str** |  | 

## Example

```python
from taikunpycore.models.partner_color_settings_dto import PartnerColorSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerColorSettingsDto from a JSON string
partner_color_settings_dto_instance = PartnerColorSettingsDto.from_json(json)
# print the JSON string representation of the object
print(PartnerColorSettingsDto.to_json())

# convert the object into a dict
partner_color_settings_dto_dict = partner_color_settings_dto_instance.to_dict()
# create an instance of PartnerColorSettingsDto from a dict
partner_color_settings_dto_from_dict = PartnerColorSettingsDto.from_dict(partner_color_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


