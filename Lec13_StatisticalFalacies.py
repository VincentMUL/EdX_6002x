# There are 3 kinds of lies: lies, damned lies, and statistics. - Mark Twain
# If you can't prove what you want to prove, demonstrate something else and pretend that they are the same thing.
# In the daze that follows the collision of statistics with the human mind, hardly anyone will notice the difference.
# - Darrell Huff, How to Lie with Statistics

# Few ways people have abused statistics.

# Anscombe's Quartet
# Statistically, the datasets are identical, but they are not.
# Plotting them shows how different they are.
# -> Statistics about the data is not the same as the data.
# -> Vizualization is key to understanding data.

# Lying with pictures
# Look at grades of students in a class.
# -> Scale of the axis
# -> Look at the axis labels, the numbers.
# Example of Fox news, not only the axis and scale, but also the data.

# GIGO (Garbage In, Garbage Out)
# On two occasions I have been asked, 'Pray, Mr. Babbage, 
# if you put into the machine wrong figures, will the right answers come out?'
# I am not able rightly to apprehend the kind of confusion of ideas that could provoke such a question.
# - Charles Babbage
#
# "The data on insanity revealed in this census is unimpeachable. 
# From it our nation must conclude that the abolition of slavery would be to the African a curse.""
# John C. Calhoun, 1840 Census
#
# John Quincy Adams protested the interpretation:
# "Atrocious misrepresentations have been made on a subject of deep importance."
# Calhoun confirmed the errors, but said they balanced each other out.
# "there were so many errors they balanced one another, and led to the same conclusion as if they were all correct"
#
# If the measurement errors were unbiased and independent of each other, 
# then we could use statistical analysis to deal with the errors.
#
# James Freeman Clarke: "It was the census that was insane, not the colored people."
# -> Analysis of bad data can lead to dangerous conclusions. GIGO!

# Airforce check returned planes during WWII on where to add armor.
# Bias from planes that returned, not the ones that didn't.
# Sampling only works well if random sampling is used.
# In simulation, we can control the data and it's easy to get real random data.
# In real world, we usually are steered by convenience.
# -> Real world data is often biased.
# A convenient sample might be representative, but there is no way of knowing if it is representative.
# Convenience samples are often biased, non-representative, and misleading.
# Another example is non-response bias.
# Presumably the people who choose not to respond are different from those who do.
# We can still do statistics despite this, but we shouldn't conclude anything about the population.
# -> Understand how the data was collected and whether or not the assumptions for the statistical tests are met.
#    If not, the results are meaningless.

# Comforting statistics, 99.8% of the firearms in the US are never used in a crime.
# Well how many are there in the US? Around 300 million. Doing the math, that's 600,000 firearms used in crimes.
# In other words, 600000 violent crimes. That's not comforting at all.
# -> Context matters! 

# Drugs X and Y for treating acne. X cures acne twice as well as Y, but X also kills twice as many patients as Y.
# Do we want X or Y? What if Y kills 0.000001% of patients and cures 50% of cases...
# -> We need to know the base rate. Percentages without a baseline are meaningless.

# Cancer cluster is a greater than expected number of cancer cases that occurs within 
# a group of people in a geographic area over a period of time. CDC
# In US about 1000 cancer clusters are reported each year.
# Only small fraction are not false alarms.
# Hypothetical example of Massachusetts (10000 sq m, 36000 new cancer cases per year)
# , 1000 cancer clusters, 1000 towns, 1 cluster per town.
# Discovered that region 111 had 143 new cancer cases over a 3 year period.
# More than 32% higher than expected. How worried should we be?
# Simulation:
import random
random.seed(0)
numCasesPerYear = 36000
numYears = 3
stateSize = 10000
communitySize = 10
numCommunities = stateSize // communitySize
numTrials = 100
numGreater = 0
for t in range(numTrials):
    locs = [0]*numCommunities
    for i in range(numCasesPerYear * numYears):
        locs[random.choice(range(numCommunities))] += 1
    if locs[111] >= 143:
        numGreater += 1
prob = round(numGreater / numTrials, 4)
print('Est. probability of observing a cluster of 143 or more cases =', prob)
# Est. probability of observing a cluster of 143 or more cases = 0.01
# Pretty low, should there be a lawsuit?
# Check Texas Sharpshooter Fallacy
# Target drawn on a barn and then shot at it or first shot at it and then drawn the target?
# We looked at a 1000 regions and looked at the one with the highest rate.
# -> We need to have a hypothesis before we look at the data.
# Instead of drawing a target around location 111, 
# we should have drawn a target around the region with the highest rate.
random.seed(0)
numCasesPerYear = 36000
numYears = 3
stateSize = 10000
communitySize = 10
numCommunities = stateSize // communitySize
numTrials = 100
numGreater = 0
for t in range(numTrials):
    locs = [0]*numCommunities
    for i in range(numCasesPerYear * numYears):
        locs[random.choice(range(numCommunities))] += 1
    if max(locs) >= 143:
        numGreater += 1
prob = round(numGreater / numTrials, 4)
print('Est. probability of observing a cluster of 143 or more cases =', prob)
# Est. probability of observing a cluster of 143 or more cases = 0.6
# -> We should not be worried at all. It's not unlikely at all.

# Cum Hoc Ergo Propter Hoc
# With this, therefore because of this.
# Humans are wired to see patterns, even when they don't exist.
# See Copenhagen doctrine, the idea that the universe is fundamentally random.
# Classic example of Lawyer spending and pet spending. Possibly no correlation at all,
# Possibly caused by a third factor, like income or increase in population.
# Number of cases of flu and school attendance. Does going to school contribute to spread of flu?
# Does the fluc contribute to school attendance? Or is there no causal relation at all? Like winter.
# Special outer coating in cold wheather, which helps with spreading the flu.
# So change of season contributes to both flu and school attendance.
# -> Correlation is not causation, we cannot conclude that one causes the other. Nor can we conclude 
#    that there is no causal relation here!!

# How do you establish causation?
# Attempt to control all variables except the one you are interested in.
# Rarely possible. Randomized controlled trials are the gold standard.
# Start with a population and randomly assign them to two groups: control and treatment.
# Deal with two groups identically except for the treatment.
#
# Example of Hormone Replacement Therapy (HRT) and heart disease.
# Observational studies showed that there was a marked reduction in risk of
# Coronary heart diseases CHD associated with postmenopausal estrogen therapy.
# Another study showed the opposite!
# More breast cancers, heart attacks, strokes and blood clots.
# -> Well conducted observational studies can be useful, but they can be misleading.
# Women taking HRT were more likely to be from groups with better than average diet and exercise habits.
# -> Randomized controlled trials are the gold standard.

# Topics handled in the course:
# Optimization problems.
# Stochastic thinking.
# Modelling aspects of the world.
# Becoming a better programmer.

# Guttag believes there are things in data analysis you can only understand by coding.
# Other courses might be more theoretical, but this course is more practical.