# -*- coding: utf-8 -*-
"""Lesson 1 - My Homework - BMW vs. Mercedes

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FGAbFqTYOmb8De8yhieGOGQUPNUW_pju
"""

!curl -s https://course.fast.ai/setup/colab | bash
  from fastai.vision import *
  from fastai.metrics import error_rate

cd '/root/.fastai/data'

from google.colab import files
files.upload()

import zipfile
zip_ref = zipfile.ZipFile('bmwmercedes.zip', 'r')
zip_ref.extractall('')
zip_ref.close()

PATH = "/root/.fastai/data/bmwmercedes"
path_img = Path(PATH)
path_img

bs = 16

fnames = get_image_files(path_img)
fnames[:5]

np.random.seed(2)
pat = re.compile(r'([^/]+)_\d+.jpg$')

# test regex
string = '/root/.fastai/data/bmwmercedes/mercedes_3.jpg'
pat.search(string).group(1)

# test ImageDataBunch inputs not empty
print(path_img)
print(fnames)
print(pat)
print(bs)
print(str(get_transforms()))

data = ImageDataBunch.from_name_re(path_img, fnames, pat, ds_tfms=get_transforms(), size=224, bs=bs)
data.normalize(imagenet_stats)

data.show_batch(rows=5, figsize=(6,10))

print(data.classes)
len(data.classes),data.c

learn = create_cnn (data, models.resnet34, metrics=error_rate)

learn.fit_one_cycle(4)

learn.save('stage-1')

interp = ClassificationInterpretation.from_learner(learn)
losses,idxs = interp.top_losses()
len(data.valid_ds)==len(losses)==len(idxs)

interp.plot_top_losses(5, figsize=(11,15))

doc(interp.plot_top_losses)

interp.plot_confusion_matrix(figsize=(12,12), dpi=60)

interp.most_confused(min_val=2)

learn.load('stage-1');

learn.lr_find()

learn.recorder.plot()

learn.unfreeze()
learn.fit_one_cycle(2, max_lr=slice(8.2e-3))

learn.save('stage-2')

learn.fit_one_cycle(4, max_lr=slice(8.2e-3))

learn.load('stage-2')

data2 = ImageDataBunch.from_name_re(path_img, fnames, pat, ds_tfms=get_transforms(),
                                   size=299, bs=bs).normalize(imagenet_stats)

learn2 = create_cnn(data, models.resnet50, metrics=error_rate)

learn2.lr_find()
learn2.recorder.plot()

learn2.save('stage-1')

learn2.fit_one_cycle(8)

learn2.save('stage1-afterFit')