import tensorflow as tf
import os
from matplotlib import pyplot as plt

# Normalize images to range [-1,1]
def normalize_photo(img):
    img = (img - 127.5) / 127.5
    return img

def normalize_sketch(img):
    img = (img - 0.5) * 2
    return img

def rand_crop(photo, sketch, height, width):
    stack_img = tf.stack([photo, sketch], axis=0)
    cropped_img = tf.image.random.crop(
        stack_img, size=[2, height, width, 3])
    
    return cropped_img[0], cropped_img[1]

def resize(photo, sketch, height, width):
  photo = tf.image.resize(photo, [height, width],
                                method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
  sketch = tf.image.resize(sketch, [height, width],
                               method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)

  return photo, sketch

@tf.function()
def rand_jitter(photo, sketch, height, width):
    photo, sketch = resize(photo, sketch, 286, 286)
    
    #Back to 256 x 256
    photo, sketch = rand_crop(photo, sketch, height, width)
    
    # 50-50 to mirror
    if tf.random.uniform(()) > 0.5:
        photo = tf.image.flip_left_right(photo)
        sketch = tf.image.flip_left_right(sketch)
    
    return photo, sketch
  
def load(photo_file):
    photo = tf.io.read_file(photo_file)
    photo = tf.io.decode_jpeg(photo)
    sketch = tf.io.read_file(os.path.splitext(photo_file)[0] + '-1.png')
    sketch = tf.io.decode_png(sketch)
    
    photo_img = tf.cast(photo, tf.float32)
    sketch_img = tf.cast(sketch, tf.float32)
    
    return photo_img, sketch_img
    
def gen_images(model, test_input, target):
    prediction = model(test_input, training=True)
    plt.figure(figsize=(15,15))
    
    display_list = [test_input[0], target[0], prediction[0]]
    titles = ['Input Image', 'Ground Truth', 'Predicted Image']
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.title(titles[i])
        plt.imshow(display_list[i] * 0.5 + 0.5)
        plt.axis('off')
    plt.show()