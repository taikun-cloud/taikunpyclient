# AiCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AiCredentialsListDto]**](AiCredentialsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.ai_credentials import AiCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of AiCredentials from a JSON string
ai_credentials_instance = AiCredentials.from_json(json)
# print the JSON string representation of the object
print(AiCredentials.to_json())

# convert the object into a dict
ai_credentials_dict = ai_credentials_instance.to_dict()
# create an instance of AiCredentials from a dict
ai_credentials_from_dict = AiCredentials.from_dict(ai_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


