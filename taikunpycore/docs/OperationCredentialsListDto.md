# OperationCredentialsListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**prometheus_username** | **str** |  | 
**prometheus_url** | **str** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**is_locked** | **bool** |  | 
**rules** | [**List[SimplePrometheusEntity]**](SimplePrometheusEntity.md) |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**is_default** | **bool** |  | 

## Example

```python
from taikunpycore.models.operation_credentials_list_dto import OperationCredentialsListDto

# TODO update the JSON string below
json = "{}"
# create an instance of OperationCredentialsListDto from a JSON string
operation_credentials_list_dto_instance = OperationCredentialsListDto.from_json(json)
# print the JSON string representation of the object
print(OperationCredentialsListDto.to_json())

# convert the object into a dict
operation_credentials_list_dto_dict = operation_credentials_list_dto_instance.to_dict()
# create an instance of OperationCredentialsListDto from a dict
operation_credentials_list_dto_from_dict = OperationCredentialsListDto.from_dict(operation_credentials_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


