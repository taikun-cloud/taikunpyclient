# FinalPriceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**yearly_final_price** | **float** |  | [optional] 
**monthly_final_price** | **float** |  | [optional] 

## Example

```python
from taikunpycore.models.final_price_dto import FinalPriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of FinalPriceDto from a JSON string
final_price_dto_instance = FinalPriceDto.from_json(json)
# print the JSON string representation of the object
print(FinalPriceDto.to_json())

# convert the object into a dict
final_price_dto_dict = final_price_dto_instance.to_dict()
# create an instance of FinalPriceDto from a dict
final_price_dto_from_dict = FinalPriceDto.from_dict(final_price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


