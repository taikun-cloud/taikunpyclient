# CredentialChartDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | **int** |  | [optional] 
**azure** | **int** |  | [optional] 
**openstack** | **int** |  | [optional] 
**google** | **int** |  | [optional] 
**tanzu** | **int** |  | [optional] 
**proxmox** | **int** |  | [optional] 
**openshift** | **int** |  | [optional] 
**vsphere** | **int** |  | [optional] 
**zadara** | **int** |  | [optional] 
**zededa** | **int** |  | [optional] 
**generic_k8_s** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from taikunpycore.models.credential_chart_dto import CredentialChartDto

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialChartDto from a JSON string
credential_chart_dto_instance = CredentialChartDto.from_json(json)
# print the JSON string representation of the object
print(CredentialChartDto.to_json())

# convert the object into a dict
credential_chart_dto_dict = credential_chart_dto_instance.to_dict()
# create an instance of CredentialChartDto from a dict
credential_chart_dto_from_dict = CredentialChartDto.from_dict(credential_chart_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


