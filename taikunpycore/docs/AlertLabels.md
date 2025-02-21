# AlertLabels


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertname** | **str** |  | [optional] 
**condition** | **str** |  | [optional] 
**container** | **str** |  | [optional] 
**endpoint** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 
**job** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**node** | **str** |  | [optional] 
**pod** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**daemonset** | **str** |  | [optional] 

## Example

```python
from taikunpycore.models.alert_labels import AlertLabels

# TODO update the JSON string below
json = "{}"
# create an instance of AlertLabels from a JSON string
alert_labels_instance = AlertLabels.from_json(json)
# print the JSON string representation of the object
print(AlertLabels.to_json())

# convert the object into a dict
alert_labels_dict = alert_labels_instance.to_dict()
# create an instance of AlertLabels from a dict
alert_labels_from_dict = AlertLabels.from_dict(alert_labels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


