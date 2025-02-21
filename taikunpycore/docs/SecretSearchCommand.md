# SecretSearchCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**search_term** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.secret_search_command import SecretSearchCommand

# TODO update the JSON string below
json = "{}"
# create an instance of SecretSearchCommand from a JSON string
secret_search_command_instance = SecretSearchCommand.from_json(json)
# print the JSON string representation of the object
print(SecretSearchCommand.to_json())

# convert the object into a dict
secret_search_command_dict = secret_search_command_instance.to_dict()
# create an instance of SecretSearchCommand from a dict
secret_search_command_from_dict = SecretSearchCommand.from_dict(secret_search_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


