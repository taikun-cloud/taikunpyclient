# TanzuCredentialsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TanzuCredentialsListDto]**](TanzuCredentialsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.tanzu_credentials_list import TanzuCredentialsList

# TODO update the JSON string below
json = "{}"
# create an instance of TanzuCredentialsList from a JSON string
tanzu_credentials_list_instance = TanzuCredentialsList.from_json(json)
# print the JSON string representation of the object
print(TanzuCredentialsList.to_json())

# convert the object into a dict
tanzu_credentials_list_dict = tanzu_credentials_list_instance.to_dict()
# create an instance of TanzuCredentialsList from a dict
tanzu_credentials_list_from_dict = TanzuCredentialsList.from_dict(tanzu_credentials_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


