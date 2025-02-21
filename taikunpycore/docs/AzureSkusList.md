# AzureSkusList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.azure_skus_list import AzureSkusList

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSkusList from a JSON string
azure_skus_list_instance = AzureSkusList.from_json(json)
# print the JSON string representation of the object
print(AzureSkusList.to_json())

# convert the object into a dict
azure_skus_list_dict = azure_skus_list_instance.to_dict()
# create an instance of AzureSkusList from a dict
azure_skus_list_from_dict = AzureSkusList.from_dict(azure_skus_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


