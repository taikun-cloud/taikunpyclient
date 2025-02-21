# MainProjectDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | [**ProjectStatus**](ProjectStatus.md) |  | [optional] 

## Example

```python
from taikunpycore.models.main_project_dto import MainProjectDto

# TODO update the JSON string below
json = "{}"
# create an instance of MainProjectDto from a JSON string
main_project_dto_instance = MainProjectDto.from_json(json)
# print the JSON string representation of the object
print(MainProjectDto.to_json())

# convert the object into a dict
main_project_dto_dict = main_project_dto_instance.to_dict()
# create an instance of MainProjectDto from a dict
main_project_dto_from_dict = MainProjectDto.from_dict(main_project_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


