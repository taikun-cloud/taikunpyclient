# AzureOffersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.azure_offers_list import AzureOffersList

# TODO update the JSON string below
json = "{}"
# create an instance of AzureOffersList from a JSON string
azure_offers_list_instance = AzureOffersList.from_json(json)
# print the JSON string representation of the object
print(AzureOffersList.to_json())

# convert the object into a dict
azure_offers_list_dict = azure_offers_list_instance.to_dict()
# create an instance of AzureOffersList from a dict
azure_offers_list_from_dict = AzureOffersList.from_dict(azure_offers_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


