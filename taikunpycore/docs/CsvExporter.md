# CsvExporter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** |  | 
**content_type** | **str** |  | 
**content** | **bytearray** |  | 

## Example

```python
from taikunpycore.models.csv_exporter import CsvExporter

# TODO update the JSON string below
json = "{}"
# create an instance of CsvExporter from a JSON string
csv_exporter_instance = CsvExporter.from_json(json)
# print the JSON string representation of the object
print(CsvExporter.to_json())

# convert the object into a dict
csv_exporter_dict = csv_exporter_instance.to_dict()
# create an instance of CsvExporter from a dict
csv_exporter_from_dict = CsvExporter.from_dict(csv_exporter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


