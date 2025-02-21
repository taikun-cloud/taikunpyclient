# ServerChartDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**azure** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**openstack** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**google** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**tanzu** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**proxmox** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**vsphere** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**zadara** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**openshift** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**zededa** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**generic_k8_s** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**failed** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**succeeded** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**waiting** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**updating** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**deleting** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**purging** | [**List[ServerCommonRecordDto]**](ServerCommonRecordDto.md) |  | [optional] 
**total_count** | **int** |  | [optional] 
**total_cpu** | **int** |  | [optional] 
**total_ram** | **int** |  | [optional] 
**total_disk_size** | **int** |  | [optional] 
**total_failed_count** | **int** |  | [optional] 
**total_succeeded_count** | **int** |  | [optional] 
**total_updating_count** | **int** |  | [optional] 
**total_pending_count** | **int** |  | [optional] 
**total_aws_count** | **int** |  | [optional] 
**total_azure_count** | **int** |  | [optional] 
**total_openstack_count** | **int** |  | [optional] 
**total_google_count** | **int** |  | [optional] 
**total_tanzu_count** | **int** |  | [optional] 
**total_openshift_count** | **int** |  | [optional] 
**total_proxmox_count** | **int** |  | [optional] 
**total_vsphere_count** | **int** |  | [optional] 
**total_zadara_count** | **int** |  | [optional] 
**total_zededa_count** | **int** |  | [optional] 
**total_generic_k8_s_count** | **int** |  | [optional] 
**used_resources** | [**List[UserResourceChartDto]**](UserResourceChartDto.md) |  | [optional] 

## Example

```python
from taikunpycore.models.server_chart_dto import ServerChartDto

# TODO update the JSON string below
json = "{}"
# create an instance of ServerChartDto from a JSON string
server_chart_dto_instance = ServerChartDto.from_json(json)
# print the JSON string representation of the object
print(ServerChartDto.to_json())

# convert the object into a dict
server_chart_dto_dict = server_chart_dto_instance.to_dict()
# create an instance of ServerChartDto from a dict
server_chart_dto_from_dict = ServerChartDto.from_dict(server_chart_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


