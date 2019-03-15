# FastAI
Practice problems and associated findings of experiments after completing the Fast.ai (2019) course by Jeremy Howard

<b>Practice - Clothing apparel image classification </b>

Goal: Classify the type of clothing item on the picture (images of size 28x28).

- normalising the images by defaults according to imagenet worsened accuracy
- applying default transforms worsened accuracy as well as training time because the transforms were not relevant to the image set. Even resnet50 had faster training time
- Leaderboard: #50 (11/3/2019) with accuracy 91.1% accuracy https://datahack.analyticsvidhya.com/contest/practice-problem-identify-the-apparels/lb

<b>Practice - Age prediction</b>

Goal: Guess the age of the person on the image. Using the IMDB dataset. Based on [Bilal Tahir's app.](https://medium.com/@btahir/a-quick-guide-to-using-regression-with-image-data-in-fastai-117304c0af90) Achieved a mean absolute error of ~ 6 years.

- for a regression task, the error_rate and accuracy metrics don't make sense. Those metrics are used for classification tasks e.g. If I classify 6 out of 10 items correctly my accuracy was 60% and error was 40%. For regression, it’s about how close you are to the correct answer and so we use metrics like MAE (mean absolute error) or MSE (mean squared error). To do that, we pass metrics = mean_absolute_error as an argument when creating the learner.
- this is also the reason why accuracy was throwing a Runtime error (which is otherwise fixable with modifying statement return (input.type(torch.cuda.FloatTensor)==targs).float().mean() )

<b>Practice - Kaggle's [Don't Overfit! II](https://www.kaggle.com/c/dont-overfit-ii/) competition</b>

Goal: With only 250 training samples, predict the probability of a binary target variable associated with each of the 20,000 rows of data.

Experimented with weight decay, dropout probability and number of hidden layers:
- a higher number of layers worked best, but there was a limit to the effect: (30,15) << (200,100) < (10000,5000) < (1000,500)
- without setting label_cls to CategoryList, it will be understood as a regression problem
- changing validation set made things a little bit worse (coincidence)
- custom regularization produced an identical score as defaults (wd = 0.3 PS = [0.01,0.1])
- higher dropout and weight decay helped (wd = 0.8 PS = [0.5])
- simplest ensemble learning: taking the mean of the best two submissions improved result
