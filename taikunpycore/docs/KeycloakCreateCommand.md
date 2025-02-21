# KeycloakCreateCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**realms_name** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.keycloak_create_command import KeycloakCreateCommand

# TODO update the JSON string below
json = "{}"
# create an instance of KeycloakCreateCommand from a JSON string
keycloak_create_command_instance = KeycloakCreateCommand.from_json(json)
# print the JSON string representation of the object
print(KeycloakCreateCommand.to_json())

# convert the object into a dict
keycloak_create_command_dict = keycloak_create_command_instance.to_dict()
# create an instance of KeycloakCreateCommand from a dict
keycloak_create_command_from_dict = KeycloakCreateCommand.from_dict(keycloak_create_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


