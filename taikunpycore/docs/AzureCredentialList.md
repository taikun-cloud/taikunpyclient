# AzureCredentialList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AzureCredentialsListDto]**](AzureCredentialsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.azure_credential_list import AzureCredentialList

# TODO update the JSON string below
json = "{}"
# create an instance of AzureCredentialList from a JSON string
azure_credential_list_instance = AzureCredentialList.from_json(json)
# print the JSON string representation of the object
print(AzureCredentialList.to_json())

# convert the object into a dict
azure_credential_list_dict = azure_credential_list_instance.to_dict()
# create an instance of AzureCredentialList from a dict
azure_credential_list_from_dict = AzureCredentialList.from_dict(azure_credential_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


