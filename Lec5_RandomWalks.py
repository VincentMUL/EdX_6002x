# Simulation Model is a description of a set of computations
# that provide useful information about the possible behaviors
# of the system being modelled.
# Usually most useful when more than one possible behavior.
# They are descriptive and not prescriptive.
# Unlike Optimization Models, which are prescriptive.
# Simulation Models are only an approximation of reality.
# "All models are wrong, but some are useful." - George Box

# Useful for mathematically intractable problems.
# Eg climate models, processor chip design, etc.
# Useful for extracting intermediat results.
# Succesive refinement: Start with a simple model and add complexity,
# to approximate reality. 
# Also great to answer What-If questions.

# Random Walks:
# Apply to many domains: stock prices, particle diffusion, etc.
# Simple to simulate, good intro to simulation.
# Also good excuse to cover some important Python concepts.
# Especially inheritance mechanisms and advanced plotting.
# Robert Brown discovered Brownian motion in 1827.
# Louis Bachelier used it to model stock prices in 1900.
# Albert Einstein wrote a paper::
# on the movement of small particles suspended in a stationary
# liquid demanded by the molecular-kinetic theory of heat.
# 
# In the drunkard's example, we'll use a 2D grid.
# Potential moves: North, South, East, West.
# We'll start at the origin (0,0).
# We'll move in a random direction; 1 step to (1,0).
# Second step can be to (0,0), (2,0), (1,1), (1,-1).
# Say we'd like to know the average distance the random walker
# is from the origin after 2 steps:
# 0.25 * 0 + 0.25 * 2 + 0.25 * (2^.5) + 0.25 * (2^.5) = +/- 1.2

# For 100000 steps, we need simulation.