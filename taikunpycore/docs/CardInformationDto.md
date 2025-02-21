# CardInformationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_month** | **str** |  | 
**expiration_year** | **str** |  | 
**last4** | **str** |  | 
**brand** | **str** |  | 
**holder_name** | **str** |  | 
**balance** | **int** |  | 

## Example

```python
from taikunpycore.models.card_information_dto import CardInformationDto

# TODO update the JSON string below
json = "{}"
# create an instance of CardInformationDto from a JSON string
card_information_dto_instance = CardInformationDto.from_json(json)
# print the JSON string representation of the object
print(CardInformationDto.to_json())

# convert the object into a dict
card_information_dto_dict = card_information_dto_instance.to_dict()
# create an instance of CardInformationDto from a dict
card_information_dto_from_dict = CardInformationDto.from_dict(card_information_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


