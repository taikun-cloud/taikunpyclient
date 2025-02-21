# AzureFlavorsWithPriceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**windows_price** | **str** |  | [optional] 
**linux_price** | **str** |  | [optional] 
**windows_spot_price** | **str** |  | [optional] 
**linux_spot_price** | **str** |  | [optional] 
**cpu** | **int** |  | [optional] 
**ram** | **float** |  | [optional] 
**description** | **object** |  | [optional] 
**max_data_disk_count** | **float** |  | [optional] 

## Example

```python
from taikunpycore.models.azure_flavors_with_price_dto import AzureFlavorsWithPriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of AzureFlavorsWithPriceDto from a JSON string
azure_flavors_with_price_dto_instance = AzureFlavorsWithPriceDto.from_json(json)
# print the JSON string representation of the object
print(AzureFlavorsWithPriceDto.to_json())

# convert the object into a dict
azure_flavors_with_price_dto_dict = azure_flavors_with_price_dto_instance.to_dict()
# create an instance of AzureFlavorsWithPriceDto from a dict
azure_flavors_with_price_dto_from_dict = AzureFlavorsWithPriceDto.from_dict(azure_flavors_with_price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


