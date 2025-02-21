# Kubesprays


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[KubesprayListDto]**](KubesprayListDto.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from taikunpycore.models.kubesprays import Kubesprays

# TODO update the JSON string below
json = "{}"
# create an instance of Kubesprays from a JSON string
kubesprays_instance = Kubesprays.from_json(json)
# print the JSON string representation of the object
print(Kubesprays.to_json())

# convert the object into a dict
kubesprays_dict = kubesprays_instance.to_dict()
# create an instance of Kubesprays from a dict
kubesprays_from_dict = Kubesprays.from_dict(kubesprays_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


