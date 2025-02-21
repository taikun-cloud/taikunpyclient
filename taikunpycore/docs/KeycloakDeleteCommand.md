# KeycloakDeleteCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.keycloak_delete_command import KeycloakDeleteCommand

# TODO update the JSON string below
json = "{}"
# create an instance of KeycloakDeleteCommand from a JSON string
keycloak_delete_command_instance = KeycloakDeleteCommand.from_json(json)
# print the JSON string representation of the object
print(KeycloakDeleteCommand.to_json())

# convert the object into a dict
keycloak_delete_command_dict = keycloak_delete_command_instance.to_dict()
# create an instance of KeycloakDeleteCommand from a dict
keycloak_delete_command_from_dict = KeycloakDeleteCommand.from_dict(keycloak_delete_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


