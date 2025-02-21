# AvailablePackagesDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_id** | **str** |  | [optional] 
**catalog_id** | **int** |  | [optional] 
**catalog_app_id** | **int** |  | [optional] 
**installed_instance_count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**normalized_name** | **str** |  | [optional] 
**logo_image_id** | **str** |  | [optional] 
**stars** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**app_version** | **str** |  | [optional] 
**deprecated** | **bool** |  | [optional] 
**signed** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**security_report_summary** | [**SecurityReportSummary**](SecurityReportSummary.md) |  | [optional] 
**ts** | **str** |  | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**is_added** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.available_packages_dto import AvailablePackagesDto

# TODO update the JSON string below
json = "{}"
# create an instance of AvailablePackagesDto from a JSON string
available_packages_dto_instance = AvailablePackagesDto.from_json(json)
# print the JSON string representation of the object
print(AvailablePackagesDto.to_json())

# convert the object into a dict
available_packages_dto_dict = available_packages_dto_instance.to_dict()
# create an instance of AvailablePackagesDto from a dict
available_packages_dto_from_dict = AvailablePackagesDto.from_dict(available_packages_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


