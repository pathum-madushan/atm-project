from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential 
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
from keras.optimizers import Adam

import logging 

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

try:
    img_width, img_height = 150, 150

    if K.image_data_format() == 'channels_first':
        input_shape = (3, img_width, img_height)
    else:
        input_shape = (img_width, img_height, 3)
    # input layer
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    logging.debug('First_Convo: {}'.format('First Layer Executed'))


    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    logging.debug('Second_Convo: {}'.format('Second Layer Executed'))



    model.add(Conv2D(64, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))
    logging.debug('Third_Convo: {}'.format('Third Layer Executed'))


    # fully connected layer
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))
    logging.debug('Fully_Convo: {}'.format('Fully Connected Layer Executed'))


    try:

        model.compile(loss='binary_crossentropy',
                    optimizer= Adam ,
                    metrics=['accuracy'])
        logging.debug('Model_Optimizing: {}'.format('Model Adam Optimized!!'))

    except:
        
        logging.error('Model_Optimizing: {}'.format('optimizer identifier Error!!'))

    train_datagenerator = ImageDataGenerator(
            rescale=1./255,
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1. / 255)

    training_flow = train_datagenerator.flow_from_directory(
        'Dataset/train',
        target_size=(img_width, img_height),
        batch_size=32,
        class_mode='binary',
        # color_mode='grayscale',
        # save_to_dir='preview',
        #  save_format='jpeg'
        )

    testing_flow = test_datagen.flow_from_directory(
            'Dataset/test',
            target_size=(img_width, img_height),
            class_mode='binary',
            # color_mode='grayscale'

    )

    model.fit_generator(
            training_flow,
            steps_per_epoch=60,
            epochs=115,
            validation_data=testing_flow,
            validation_steps=11)

    # to save model weights
    model.save_weights('./models/save_model20.h5')
    logging.info('Model_Saved: {}'.format('Model saved successfully!!'))
except:
    logging.error('keyboard intercepted: {}'.format('keyboard intercepted Error!!'))



