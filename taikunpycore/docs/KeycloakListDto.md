# KeycloakListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**url** | **str** |  | 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**realms_name** | **str** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**partner_logo** | **str** |  | 
**enabled** | **bool** |  | 

## Example

```python
from taikunpycore.models.keycloak_list_dto import KeycloakListDto

# TODO update the JSON string below
json = "{}"
# create an instance of KeycloakListDto from a JSON string
keycloak_list_dto_instance = KeycloakListDto.from_json(json)
# print the JSON string representation of the object
print(KeycloakListDto.to_json())

# convert the object into a dict
keycloak_list_dto_dict = keycloak_list_dto_instance.to_dict()
# create an instance of KeycloakListDto from a dict
keycloak_list_dto_from_dict = KeycloakListDto.from_dict(keycloak_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


