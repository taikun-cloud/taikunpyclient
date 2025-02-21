# GoogleCredentialList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GoogleCredentialsListDto]**](GoogleCredentialsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.google_credential_list import GoogleCredentialList

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCredentialList from a JSON string
google_credential_list_instance = GoogleCredentialList.from_json(json)
# print the JSON string representation of the object
print(GoogleCredentialList.to_json())

# convert the object into a dict
google_credential_list_dict = google_credential_list_instance.to_dict()
# create an instance of GoogleCredentialList from a dict
google_credential_list_from_dict = GoogleCredentialList.from_dict(google_credential_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


