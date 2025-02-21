# TaikunLbResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**public_ip** | **str** |  | 
**virtual_lb_ip_first** | **str** |  | 
**virtual_lb_ip_second** | **str** |  | 
**private_ip_first** | **str** |  | 
**private_ip_second** | **str** |  | 
**virtual_router_id** | **str** |  | 
**hypervisor_first** | **str** |  | 
**hypervisor_second** | **str** |  | 
**svc_name** | **str** |  | 
**svc_namespace** | **str** |  | 
**project_name** | **str** |  | 

## Example

```python
from taikunpycore.models.taikun_lb_response_dto import TaikunLbResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaikunLbResponseDto from a JSON string
taikun_lb_response_dto_instance = TaikunLbResponseDto.from_json(json)
# print the JSON string representation of the object
print(TaikunLbResponseDto.to_json())

# convert the object into a dict
taikun_lb_response_dto_dict = taikun_lb_response_dto_instance.to_dict()
# create an instance of TaikunLbResponseDto from a dict
taikun_lb_response_dto_from_dict = TaikunLbResponseDto.from_dict(taikun_lb_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


