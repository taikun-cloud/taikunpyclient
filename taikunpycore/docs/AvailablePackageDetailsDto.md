# AvailablePackageDetailsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**app_repo_name** | **str** |  | [optional] 
**app_repo_organization_name** | **str** |  | [optional] 
**app_repo_id** | **str** |  | [optional] 
**package_id** | **str** |  | [optional] 
**logo_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**readme** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**security_report** | [**SecurityReportSummaryDto**](SecurityReportSummaryDto.md) |  | [optional] 
**app_version** | **str** |  | [optional] 
**stars** | **int** |  | [optional] 
**verified_publisher** | **bool** |  | [optional] 
**official** | **bool** |  | [optional] 
**bound_catalogs** | [**List[CommonDropdownDto]**](CommonDropdownDto.md) |  | [optional] 
**has_json_schema** | **bool** |  | [optional] 

## Example

```python
from taikunpycore.models.available_package_details_dto import AvailablePackageDetailsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AvailablePackageDetailsDto from a JSON string
available_package_details_dto_instance = AvailablePackageDetailsDto.from_json(json)
# print the JSON string representation of the object
print(AvailablePackageDetailsDto.to_json())

# convert the object into a dict
available_package_details_dto_dict = available_package_details_dto_instance.to_dict()
# create an instance of AvailablePackageDetailsDto from a dict
available_package_details_dto_from_dict = AvailablePackageDetailsDto.from_dict(available_package_details_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


