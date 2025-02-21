# OperationCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OperationCredentialsListDto]**](OperationCredentialsListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.operation_credentials import OperationCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of OperationCredentials from a JSON string
operation_credentials_instance = OperationCredentials.from_json(json)
# print the JSON string representation of the object
print(OperationCredentials.to_json())

# convert the object into a dict
operation_credentials_dict = operation_credentials_instance.to_dict()
# create an instance of OperationCredentials from a dict
operation_credentials_from_dict = OperationCredentials.from_dict(operation_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


