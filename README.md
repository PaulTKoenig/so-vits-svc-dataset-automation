# so-vits-svc-dataset-automation
This project automates the process of creating a dataset for training a so-vits-svc model with youtube audio.


How to run:

Create a directory similar to 'Example' directory with a text file named 'urls.txt'.

Add youtube urls, each on a new line.

Run main.py.

Enter the name of your directory.



Output:
Each audio clip will be in your directory.
silenced_vocals holds each audio clip with silence removed.
complete_dataset holds each audio clip split into 10 second increments.
