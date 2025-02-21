# PartnerDetailsForUserDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**logo** | **str** |  | 
**link** | **str** |  | 
**domain** | **str** |  | 
**id** | **int** |  | 

## Example

```python
from taikunpycore.models.partner_details_for_user_dto import PartnerDetailsForUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of PartnerDetailsForUserDto from a JSON string
partner_details_for_user_dto_instance = PartnerDetailsForUserDto.from_json(json)
# print the JSON string representation of the object
print(PartnerDetailsForUserDto.to_json())

# convert the object into a dict
partner_details_for_user_dto_dict = partner_details_for_user_dto_instance.to_dict()
# create an instance of PartnerDetailsForUserDto from a dict
partner_details_for_user_dto_from_dict = PartnerDetailsForUserDto.from_dict(partner_details_for_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


