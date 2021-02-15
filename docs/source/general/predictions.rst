
.. _predictions:

#######################
Predictions (inference)
#######################

You can use Flash to get predictions on pretrained or finetuned models.

Predict on a single sample of data
==================================

You can pass in a sample of data (image file path, a string of text, etc) to the :func:`~flash.core.model.Task.predict` method.

	
.. code-block:: python

	from flash import Trainer
	from flash.core.data import download_data
	from flash.vision import ImageClassificationData, ImageClassifier


	# 1. Download the data set
	download_data("https://pl-flash-data.s3.amazonaws.com/hymenoptera_data.zip", 'data/')

	# 2. Load the model from a checkpoint
	model = ImageClassifier.load_from_checkpoint("https://flash-weights.s3.amazonaws.com/image_classification_model.pt")

	# 3. Predict whether the image contains an ant or a bee
	predictions = model.predict("data/hymenoptera_data/val/bees/65038344_52a45d090d.jpg")
	print(predictions)



Predict on a csv file
=====================

.. code-block:: python

	from flash.core.data import download_data
	from flash.tabular import TabularClassifier

	# 1. Download the data
	download_data("https://pl-flash-data.s3.amazonaws.com/titanic.zip", 'data/')

	# 2. Load the model from a checkpoint
	model = TabularClassifier.load_from_checkpoint(
	    "https://flash-weights.s3.amazonaws.com/tabnet_classification_model.pt"
	)

	# 3. Generate predictions from a csv file! Who would survive?
	predictions = model.predict("data/titanic/titanic.csv")
	print(predictions)


