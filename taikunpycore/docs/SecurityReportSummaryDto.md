# SecurityReportSummaryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**low** | **int** |  | [optional] 
**high** | **int** |  | [optional] 
**medium** | **int** |  | [optional] 
**unknown** | **int** |  | [optional] 
**critical** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.security_report_summary_dto import SecurityReportSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityReportSummaryDto from a JSON string
security_report_summary_dto_instance = SecurityReportSummaryDto.from_json(json)
# print the JSON string representation of the object
print(SecurityReportSummaryDto.to_json())

# convert the object into a dict
security_report_summary_dto_dict = security_report_summary_dto_instance.to_dict()
# create an instance of SecurityReportSummaryDto from a dict
security_report_summary_dto_from_dict = SecurityReportSummaryDto.from_dict(security_report_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


