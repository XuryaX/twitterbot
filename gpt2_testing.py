"""
Testing GPT-2 integration
"""

import tensorflow as tf
import gpt_2_simple as gpt2

# Download medium model
# gpt2.download_gpt2(model_name='345M')

tf.config.experimental.list_physical_devices('GPU')

sess = gpt2.start_tf_sess()
single_text = gpt2.generate(sess, return_as_list=True)[0]
print(single_text)
