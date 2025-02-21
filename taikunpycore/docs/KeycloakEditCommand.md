# KeycloakEditCommand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**realms_name** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.keycloak_edit_command import KeycloakEditCommand

# TODO update the JSON string below
json = "{}"
# create an instance of KeycloakEditCommand from a JSON string
keycloak_edit_command_instance = KeycloakEditCommand.from_json(json)
# print the JSON string representation of the object
print(KeycloakEditCommand.to_json())

# convert the object into a dict
keycloak_edit_command_dict = keycloak_edit_command_instance.to_dict()
# create an instance of KeycloakEditCommand from a dict
keycloak_edit_command_from_dict = KeycloakEditCommand.from_dict(keycloak_edit_command_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


