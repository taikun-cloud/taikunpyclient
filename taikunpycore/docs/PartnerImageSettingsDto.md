# PartnerImageSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expanded** | **str** |  | 
**collapsed** | **str** |  | 

## Example

```python
from taikunpycore.models.partner_image_settings_dto import PartnerImageSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerImageSettingsDto from a JSON string
partner_image_settings_dto_instance = PartnerImageSettingsDto.from_json(json)
# print the JSON string representation of the object
print(PartnerImageSettingsDto.to_json())

# convert the object into a dict
partner_image_settings_dto_dict = partner_image_settings_dto_instance.to_dict()
# create an instance of PartnerImageSettingsDto from a dict
partner_image_settings_dto_from_dict = PartnerImageSettingsDto.from_dict(partner_image_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


