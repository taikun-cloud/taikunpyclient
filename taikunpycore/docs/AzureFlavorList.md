# AzureFlavorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AzureFlavorsWithPriceDto]**](AzureFlavorsWithPriceDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.azure_flavor_list import AzureFlavorList

# TODO update the JSON string below
json = "{}"
# create an instance of AzureFlavorList from a JSON string
azure_flavor_list_instance = AzureFlavorList.from_json(json)
# print the JSON string representation of the object
print(AzureFlavorList.to_json())

# convert the object into a dict
azure_flavor_list_dict = azure_flavor_list_instance.to_dict()
# create an instance of AzureFlavorList from a dict
azure_flavor_list_from_dict = AzureFlavorList.from_dict(azure_flavor_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


