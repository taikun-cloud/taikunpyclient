# ServerTemplateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**CloudRole**](CloudRole.md) |  | [optional] 
**flavor** | **str** |  | [optional] 
**disk_size** | **float** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.server_template_dto import ServerTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerTemplateDto from a JSON string
server_template_dto_instance = ServerTemplateDto.from_json(json)
# print the JSON string representation of the object
print(ServerTemplateDto.to_json())

# convert the object into a dict
server_template_dto_dict = server_template_dto_instance.to_dict()
# create an instance of ServerTemplateDto from a dict
server_template_dto_from_dict = ServerTemplateDto.from_dict(server_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


