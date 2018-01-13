
from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
from keras.optimizers import SGD, RMSprop

from cnn_functions import rate_scheduler, train_model_sample
from model_zoo import bn_feature_net_61x61 as the_model

import os
import datetime
import numpy as np

batch_size = 256
n_epoch = 25

dataset = "3T3_all_61x61"
expt = "bn_feature_net_61x61"

direc_save = "/home/DeepCell/trained_networks_new/"
direc_data = "/home//DeepCell/training_data_npz/"

optimizer = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
lr_sched = rate_scheduler(lr = 0.01, decay = 0.95)

for iterate in xrange(5):

	model = the_model(n_features = 3, n_channels = 2, reg = 1e-5)

	train_model_sample(model = model, dataset = dataset, optimizer = optimizer, 
		expt = expt, it = iterate, batch_size = batch_size, n_epoch = n_epoch,
		direc_save = direc_save, 
		direc_data = direc_data, 
		lr_sched = lr_sched,
		rotate = True, flip = True, shear = False)

	del model
	from keras.backend.common import _UID_PREFIXES
	for key in _UID_PREFIXES.keys():
		_UID_PREFIXES[key] = 0