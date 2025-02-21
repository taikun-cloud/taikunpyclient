# KubesprayListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**version** | **str** |  | 
**kubernetes_version** | **str** |  | 
**is_deprecated** | **bool** |  | 

## Example

```python
from taikunpycore.models.kubespray_list_dto import KubesprayListDto

# TODO update the JSON string below
json = "{}"
# create an instance of KubesprayListDto from a JSON string
kubespray_list_dto_instance = KubesprayListDto.from_json(json)
# print the JSON string representation of the object
print(KubesprayListDto.to_json())

# convert the object into a dict
kubespray_list_dto_dict = kubespray_list_dto_instance.to_dict()
# create an instance of KubesprayListDto from a dict
kubespray_list_dto_from_dict = KubesprayListDto.from_dict(kubespray_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


