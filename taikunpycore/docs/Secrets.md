# Secrets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SecretDto]**](SecretDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.secrets import Secrets

# TODO update the JSON string below
json = "{}"
# create an instance of Secrets from a JSON string
secrets_instance = Secrets.from_json(json)
# print the JSON string representation of the object
print(Secrets.to_json())

# convert the object into a dict
secrets_dict = secrets_instance.to_dict()
# create an instance of Secrets from a dict
secrets_from_dict = Secrets.from_dict(secrets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


