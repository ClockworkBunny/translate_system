## Product Title Translation System from English to Thai
The data file is "Product MT - Data.excel" provided by Shopee
### Requirements
Code is written in Python (2.7) and requires the following packages (only uncommon ones):
1 mstranslator
https://pypi.python.org/pypi/mstranslator
2 google
https://github.com/BirdAPI/Google-Search-API

In addition, a collection of seed product titles should be provided in resource\prodcut_names.txt. 


### Running the models

```
python main.py key
```

where key is the key to access Bing translation API. In the main.py, the input corpus is used as the "sample-data" in the excel file. It will generate the translated titles in Thai and store them in the "Output.txt".


### Example output
result_1.txt and result_2.txt are the translated titles corresponding to 'Sample-Data' and 'Test-Data' in the excel file. 
