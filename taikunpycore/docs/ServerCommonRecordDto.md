# ServerCommonRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | [optional] 
**project_name** | **str** |  | [optional] 
**names** | **List[str]** |  | [optional] 

## Example

```python
from taikunpycore.models.server_common_record_dto import ServerCommonRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerCommonRecordDto from a JSON string
server_common_record_dto_instance = ServerCommonRecordDto.from_json(json)
# print the JSON string representation of the object
print(ServerCommonRecordDto.to_json())

# convert the object into a dict
server_common_record_dto_dict = server_common_record_dto_instance.to_dict()
# create an instance of ServerCommonRecordDto from a dict
server_common_record_dto_from_dict = ServerCommonRecordDto.from_dict(server_common_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


