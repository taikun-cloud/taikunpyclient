# ZadaraCredentialList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ZadaraCredentialsListDto]**](ZadaraCredentialsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.zadara_credential_list import ZadaraCredentialList

# TODO update the JSON string below
json = "{}"
# create an instance of ZadaraCredentialList from a JSON string
zadara_credential_list_instance = ZadaraCredentialList.from_json(json)
# print the JSON string representation of the object
print(ZadaraCredentialList.to_json())

# convert the object into a dict
zadara_credential_list_dict = zadara_credential_list_instance.to_dict()
# create an instance of ZadaraCredentialList from a dict
zadara_credential_list_from_dict = ZadaraCredentialList.from_dict(zadara_credential_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


