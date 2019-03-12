# FastAI
Homeworks and experiments from the Fast.ai (2019) course by Jeremy Howard

<b>Practice Apparel problem findings</b>
- normalising the images by defaults according to imagenet worsened accuracy
- applying default transforms worsened accuracy as well as training time because the transforms were not relevant to the image set. Even resnet50 had faster training time
- Leaderboard: #50 (11/3/2019) with accuracy 91.1% accuracy https://datahack.analyticsvidhya.com/contest/practice-problem-identify-the-apparels/lb

<b>Practice Age detection problem findings</b>
- for a regression task, the error_rate and accuracy metrics don't make sense. Those metrics are used for classification tasks e.g. If I classify 6 out of 10 items correctly my accuracy was 60% and error was 40%. For regression, it’s about how close you are to the correct answer and so we use metrics like MAE (mean absolute error) or MSE (mean squared error). To do that, we pass metrics = mean_absolute_error as an argument when creating the learner.
