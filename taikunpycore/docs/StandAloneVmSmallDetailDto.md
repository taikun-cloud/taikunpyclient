# StandAloneVmSmallDetailDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**project_id** | **int** |  | 

## Example

```python
from taikunpycore.models.stand_alone_vm_small_detail_dto import StandAloneVmSmallDetailDto

# TODO update the JSON string below
json = "{}"
# create an instance of StandAloneVmSmallDetailDto from a JSON string
stand_alone_vm_small_detail_dto_instance = StandAloneVmSmallDetailDto.from_json(json)
# print the JSON string representation of the object
print(StandAloneVmSmallDetailDto.to_json())

# convert the object into a dict
stand_alone_vm_small_detail_dto_dict = stand_alone_vm_small_detail_dto_instance.to_dict()
# create an instance of StandAloneVmSmallDetailDto from a dict
stand_alone_vm_small_detail_dto_from_dict = StandAloneVmSmallDetailDto.from_dict(stand_alone_vm_small_detail_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


