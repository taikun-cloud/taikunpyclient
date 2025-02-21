# SecurityReportSummary


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
from taikunpycore.models.security_report_summary import SecurityReportSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityReportSummary from a JSON string
security_report_summary_instance = SecurityReportSummary.from_json(json)
# print the JSON string representation of the object
print(SecurityReportSummary.to_json())

# convert the object into a dict
security_report_summary_dict = security_report_summary_instance.to_dict()
# create an instance of SecurityReportSummary from a dict
security_report_summary_from_dict = SecurityReportSummary.from_dict(security_report_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


