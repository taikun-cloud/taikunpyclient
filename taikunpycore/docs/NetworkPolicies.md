# NetworkPolicies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NetworkPolicyDto]**](NetworkPolicyDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.network_policies import NetworkPolicies

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkPolicies from a JSON string
network_policies_instance = NetworkPolicies.from_json(json)
# print the JSON string representation of the object
print(NetworkPolicies.to_json())

# convert the object into a dict
network_policies_dict = network_policies_instance.to_dict()
# create an instance of NetworkPolicies from a dict
network_policies_from_dict = NetworkPolicies.from_dict(network_policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


