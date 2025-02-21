# CloudCredentialsDropdownRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**cloud_type** | [**CloudType**](CloudType.md) |  | 
**projects** | [**List[ProjectWithFlavorsAndImagesDto]**](ProjectWithFlavorsAndImagesDto.md) |  | 

## Example

```python
from taikunpycore.models.cloud_credentials_dropdown_record_dto import CloudCredentialsDropdownRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of CloudCredentialsDropdownRecordDto from a JSON string
cloud_credentials_dropdown_record_dto_instance = CloudCredentialsDropdownRecordDto.from_json(json)
# print the JSON string representation of the object
print(CloudCredentialsDropdownRecordDto.to_json())

# convert the object into a dict
cloud_credentials_dropdown_record_dto_dict = cloud_credentials_dropdown_record_dto_instance.to_dict()
# create an instance of CloudCredentialsDropdownRecordDto from a dict
cloud_credentials_dropdown_record_dto_from_dict = CloudCredentialsDropdownRecordDto.from_dict(cloud_credentials_dropdown_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


