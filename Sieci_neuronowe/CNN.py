import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
import matplotlib.pyplot as plt

# Zmodyfikuj ścieżkę zgodnie z lokalizacją Twojego pliku z danymi
DATA_PATH = "data.json"

def load_data(data_path):
    """Loads training dataset from json file.
    :param data_path: Path to json file containing data
    :return: Inputs (X) and targets (y)
    """
    with open(data_path, "r") as fp:
        data = json.load(fp)

    # Assume that our data file has 'pcp' and 'labels' keys
    X = np.array(data["pcp"])
    y = np.array(data["labels"])
    return X, y

def prepare_datasets(test_size, validation_size):
    """Splits data into training, validation, and test sets.
    :param test_size: Percentage of data set to allocate to test split
    :param validation_size: Percentage of training set to allocate to validation split
    :return: Training, validation, and test sets
    """
    X, y = load_data(DATA_PATH)

    # Split dataset into training and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    # Split training set into training and validation
    X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=validation_size)

    # Add an axis to input sets
    X_train = X_train[..., np.newaxis]
    X_validation = X_validation[..., np.newaxis]
    X_test = X_test[..., np.newaxis]

    return X_train, X_validation, X_test, y_train, y_validation, y_test

def build_model(input_shape):
    """Builds a neural network model
    :param input_shape: Shape of input data
    :return: Compiled CNN model
    """
    model = keras.Sequential()

    # Flatten the input layer
    model.add(keras.layers.Flatten(input_shape=input_shape))

    # First dense layer
    model.add(keras.layers.Dense(512, activation='relu'))
    model.add(keras.layers.Dropout(0.3))

    # Second dense layer
    model.add(keras.layers.Dense(512, activation='relu'))
    model.add(keras.layers.Dropout(0.3))

    # Third dense layer
    model.add(keras.layers.Dense(64, activation='relu'))

    # Output layer
    model.add(keras.layers.Dense(11, activation='softmax'))  # Assuming 10 classes

    return model

def plot_history(history):
    """Plots accuracy/loss for training/validation set as a function of the epochs
    :param history: Training history of model
    """
    fig, axs = plt.subplots(2)

    # Create accuracy subplot
    axs[0].plot(history.history['accuracy'], label='train accuracy')
    axs[0].plot(history.history['val_accuracy'], label='test accuracy')
    axs[0].set_ylabel('Accuracy')
    axs[0].legend(loc='lower right')
    axs[0].set_title('Accuracy eval')

    # Create error subplot
    axs[1].plot(history.history['loss'], label='train loss')
    axs[1].plot(history.history['val_loss'], label='test loss')
    axs[1].set_ylabel('Loss')
    axs[1].set_xlabel('Epoch')
    axs[1].legend(loc='upper right')
    axs[1].set_title('Loss eval')

    plt.show()

if __name__ == "__main__":
    X_train, X_validation, X_test, y_train, y_validation, y_test = prepare_datasets(0.25, 0.2)

    input_shape = (X_train.shape[1], X_train.shape[2], 1)  # Assuming data is in [num_samples, num_pcp_features, 1]
    model = build_model(input_shape)

    # Compile the model
    optimiser = keras.optimizers.Adam(learning_rate=0.0001)
    model.compile(optimizer=optimiser, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # Print model summary
    model.summary()

    # Train the model
    history = model.fit(X_train, y_train, validation_data=(X_validation, y_validation), batch_size=32, epochs=200)

    # Plot accuracy and loss
    plot_history(history)

    model_save_path = 'model.h5'  # Zapisuje model w formacie HDF5
    model.save(model_save_path)

    # Evaluate the model on the test set
    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
    print('\nTest accuracy:', test_acc)