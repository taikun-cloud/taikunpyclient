# CreateGenericTaikunLbDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**svc_name** | **str** |  | [optional] 
**svc_namespace** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.create_generic_taikun_lb_dto import CreateGenericTaikunLbDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGenericTaikunLbDto from a JSON string
create_generic_taikun_lb_dto_instance = CreateGenericTaikunLbDto.from_json(json)
# print the JSON string representation of the object
print(CreateGenericTaikunLbDto.to_json())

# convert the object into a dict
create_generic_taikun_lb_dto_dict = create_generic_taikun_lb_dto_instance.to_dict()
# create an instance of CreateGenericTaikunLbDto from a dict
create_generic_taikun_lb_dto_from_dict = CreateGenericTaikunLbDto.from_dict(create_generic_taikun_lb_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


