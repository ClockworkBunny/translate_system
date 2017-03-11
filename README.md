## Product Title Translation System from English to Thai
Code for the paper [Convolutional Neural Networks for Sentence Classification](http://arxiv.org/abs/1408.5882) (EMNLP 2014).

Runs the model on Pang and Lee's movie review dataset (MR in the paper).
Please cite the original paper when using the data.

### Requirements
Code is written in Python (2.7) and requires the following packages (only uncommon ones):
1 mstranslator
https://pypi.python.org/pypi/mstranslator
2 google
https://github.com/BirdAPI/Google-Search-API

In addition, a collection of seed product titles should be provided in resource\prodcut_names.txt. And to access the bing translator API, a key should be provided in the main.py file.


### Running the models

```
python main.py 
```

where path points to the word2vec binary file (i.e. `GoogleNews-vectors-negative300.bin` file). 
This will create a pickle object called `mr.p` in the same folder, which contains the dataset
in the right format.

Note: This will create the dataset with different fold-assignments than was used in the paper.
You should still be getting a CV score of >81% with CNN-nonstatic model, though.


### Example output
result
