# OpenshiftListDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**base_domain** | **str** |  | 
**storage_class** | **str** |  | 
**organization_id** | **int** |  | 
**organization_name** | **str** |  | 
**projects** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | 
**project_count** | **int** |  | 
**is_locked** | **bool** |  | 
**created_by** | **str** |  | 
**last_modified** | **str** |  | 
**last_modified_by** | **str** |  | 
**is_default** | **bool** |  | 
**created_at** | **str** |  | 
**continent_name** | **str** |  | 

## Example

```python
from taikunpycore.models.openshift_list_dto import OpenshiftListDto

# TODO update the JSON string below
json = "{}"
# create an instance of OpenshiftListDto from a JSON string
openshift_list_dto_instance = OpenshiftListDto.from_json(json)
# print the JSON string representation of the object
print(OpenshiftListDto.to_json())

# convert the object into a dict
openshift_list_dto_dict = openshift_list_dto_instance.to_dict()
# create an instance of OpenshiftListDto from a dict
openshift_list_dto_from_dict = OpenshiftListDto.from_dict(openshift_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


