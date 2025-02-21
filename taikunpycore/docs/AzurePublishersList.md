# AzurePublishersList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.azure_publishers_list import AzurePublishersList

# TODO update the JSON string below
json = "{}"
# create an instance of AzurePublishersList from a JSON string
azure_publishers_list_instance = AzurePublishersList.from_json(json)
# print the JSON string representation of the object
print(AzurePublishersList.to_json())

# convert the object into a dict
azure_publishers_list_dict = azure_publishers_list_instance.to_dict()
# create an instance of AzurePublishersList from a dict
azure_publishers_list_from_dict = AzurePublishersList.from_dict(azure_publishers_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


