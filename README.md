# AreYouMad?

A powerful python script to find toxic messages using TensorFlow.

## Things to know

### How Big Is The Data Set?

- 140MB when unziped.

### Can I Save The Model?

- Yes! by entering "y" when promted to save the model you will save the model to the current directory.
- Currently, the script is unable to use a saved model.
  - This will be added soon.


### How long will this take to run?

- For my laptop (Maxed out 2022 M2 Macbook Air), it took around 10 minutes to do 100 Epochs.
- The time the script takes is dependent on the `epochs` variable.

### Is There Anything Explict In The Data?

- Yes, because the data comes from wikipedia users, their are a large amount of hatful and inaproprate messages.
- I do not support any of the hateful messages in the data.

### Where Does The Data Come From?

- [Here!](https://www.kaggle.com/c/jigsaw-multilingual-toxic-comment-classification/data)

### Required Libarys

- Tensorflow (2.14.0+)
- Numpy
- Matplotlib

- To install, run:
  - `pip install tensorflow`
  - `pip install numpy`
  - `pip install matplotlib`

  - For OSX/MacOS replace `pip` with `pip3`

### Its Not Working!

- Use the `examples` list to input your messages.
- Dont forget to run the `OrganiseData.py` file to format and organize the data set!
- Make sure you unzip the data before use.
- Run the python file as a notebook (.ipynb).
