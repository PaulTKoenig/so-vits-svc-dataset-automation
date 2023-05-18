# so-vits-svc-dataset-automation
This project automates the process of creating a dataset for training a so-vits-svc model with youtube audio.


How to run:

1. Create a directory similar to 'Example' directory with a text file named 'urls.txt'.

2. Add youtube urls, each on a new line.

3. Run main.py.

4. Enter the name of your directory.



Output:

1. Each audio clip will be in your directory.

2. silenced_vocals holds each audio clip with silence removed.

3. complete_dataset holds each audio clip split into 10 second increments.
