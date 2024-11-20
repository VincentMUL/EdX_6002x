# Vizualizing results:
# there are different orders of growth of procedures
# used graphs to provide an intuitive sense of the differences
# example of leveraging an existing library instead of starting from scratch:
# graphing, numerical computation and stochastic computation


import pylab as plt #import the library as plt short for plot

#example from book
# plt.figure(1) #create figure 1
# plt.plot([1,2,3,4], [1,7,3,5]) #draw on figure 1
# plt.show() #show figure 1

# simplest pylab function is plotting two lists x and y
# more advanced include arrays; x = np.array([1,2,3,4]) and y = np.array([1,7,3,5])
# first we'll focus on lists
#generating some data, some samples
mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []
for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i) #choose 1.5 to make it visual

# plt.plot(mySamples, myLinear) #generate the plot with the linear data
# # arguments are lists of values and NEED to be of the same length
# # calling function in an iPython console will generate plots within that console
# # calling function in a Python console will create a sperate window 
# # plt.show() #show the plot

# # display all graphs of different orders of growth:
# plt.plot(mySamples, myQuadratic)
# plt.plot(mySamples, myCubic)
# plt.plot(mySamples, myExponential)
# plt.show() #show the plot

# # # problem: linear and quadratic are hard to distinguish; scales of the graphs change so rapidly
# # # graph each one separately to see the differences
# # # plt.figure(<arg>) #create figure 'lin', name that allows reference
# plt.figure('lin') #create figure 'lin'
# plt.plot(mySamples, myLinear)
# plt.show() #show the plot
# plt.figure('quad') #create figure 'quad'
# plt.plot(mySamples, myQuadratic)
# plt.show() #show the plot
# plt.figure('cube') #create figure 'cube'
# plt.plot(mySamples, myCubic)
# plt.show() #show the plot
# plt.figure('expo') #create figure 'expo'
# plt.plot(mySamples, myExponential)
# plt.show() #show the plot

# #Important to label plots! 
# plt.figure('lin') #create figure 'lin'
# plt.xlabel('sample points') #label x-axis
# plt.ylabel('linear function') #label y-axis
# plt.plot(mySamples, myLinear)
# # plt.show() #show the plot 
# plt.figure('quad') #create figure 'quad'
# plt.xlabel('sample points') #label x-axis
# plt.ylabel('quadratic function') #label y-axis
# plt.plot(mySamples, myQuadratic)
# # plt.show() #show the plot
# plt.figure('cube') #create figure 'cube'
# plt.xlabel('sample points') #label x-axis
# plt.ylabel('cubic function') #label y-axis
# plt.plot(mySamples, myCubic)
# # plt.show() #show the plot
# plt.figure('expo') #create figure 'expo'
# plt.xlabel('sample points') #label x-axis
# plt.ylabel('exponential function') #label y-axis
# plt.plot(mySamples, myExponential)
# # plt.show() #show the plot

# #it is possible to open a figure and plot them and then to change labelling/titling afterwards;
# #just by reopening each figure and adding a title/label
# plt.figure('lin')
# plt.title('Linear')
# plt.figure('quad')
# plt.clf() #clear the frame, plot before, so no plot now!
# #if only clearing the labels, put before the plot
# plt.title('Quadratic')
# plt.figure('cube')
# plt.title('Cubic')
# plt.figure('expo')
# plt.title('Exponential')
# plt.show() #show the plot
# #this is by reusing previous windows, 
# #if you want to clean up the windows, you can use plt.clf() (clear frame)
# #to clear the figure
# #plot colour always default per image, control with arguments

# #if we want to compare; multiple functions on same display (but scale!)
# #or set limits on the axes
# plt.figure('lin')
# plt.clf() #clear the frame
# plt.ylim(0,1000) #set y-axis limits
# plt.plot(mySamples, myLinear)
# plt.figure('quad')
# plt.clf() #clear the frame
# plt.ylim(0,1000) #set y-axis limits
# plt.plot(mySamples, myQuadratic)
# plt.figure('lin')
# plt.title('Linear')
# plt.figure('quad')
# plt.title('Quadratic')
# plt.show() #notice the very clear difference in graphs

# #overlaying plots and pick plots to see
# plt.figure('lin quad')
# plt.clf() #clear the frame
# plt.plot(mySamples, myLinear)
# plt.plot(mySamples, myQuadratic)

# plt.figure('cube expo')
# plt.clf() #clear the frame
# plt.plot(mySamples, myCubic)
# plt.plot(mySamples, myExponential)
# plt.figure('lin quad')
# plt.title('Linear vs Quadratic')
# plt.figure('cube expo')
# plt.title('Cubic vs Exponential')
# plt.show() #notice how cubic and exponential cross and change growth rates
# #also notice scales!
# #add labels to the plots to make it clear what is being displayed
# plt.figure('lin quad')
# plt.clf() #clear the frame
# plt.plot(mySamples, myLinear, label = 'linear')
# plt.plot(mySamples, myQuadratic, label = 'quadratic')
# plt.legend(loc = 'upper left') #display the labels in specified location
# plt.title('Linear vs Quadratic')

# plt.figure('cube expo')
# plt.clf() #clear the frame
# plt.plot(mySamples, myCubic, label = 'cubic')
# plt.plot(mySamples, myExponential, label = 'exponential')
# plt.legend() #display the labels in default/best location
# plt.title('Cubic vs Exponential')
# plt.show()

# #CHANGING DATA DISPLAY:
# plt.figure('lin quad')
# plt.clf() #clear the frame
# plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0) #blue line
# plt.plot(mySamples, myQuadratic, 'ro', label = 'quadratic', linewidth = 3.0) #red circles
# plt.legend(loc = 'upper left') #display the labels in specified location
# plt.title('Linear vs Quadratic')

# plt.figure('cube expo')
# plt.clf() #clear the frame
# plt.plot(mySamples, myCubic, 'g^', label = 'cubic', linewidth = 4.0) #green triangles
# plt.plot(mySamples, myExponential, 'r--', label = 'exponential', linewidth = 5.0) #red dashed line
# plt.legend()
# plt.title('Cubic vs Exponential')
# plt.show()

# #USING SUBPLOTS:
# plt.figure('lin quad')
# plt.clf() #clear the frame
# plt.subplot(211) #2 rows, 1 column, 1st plot
# plt.ylim(0,900) #set y-axis limits
# plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0) #blue line
# plt.subplot(212) #2 rows, 1 column, 2nd plot
# plt.ylim(0,900) #set y-axis limits
# plt.plot(mySamples, myQuadratic, 'r', label = 'quadratic', linewidth = 3.0) #red circles
# plt.legend(loc = 'upper left') #display the labels in specified location
# plt.title('Linear vs Quadratic')

# plt.figure('cube expo')
# plt.clf() #clear the frame
# plt.subplot(121) #1 row, 2 columns, 1st plot
# plt.ylim(0,140000) #set y-axis limits within each subplot
# plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 4.0) #green triangles
# plt.subplot(122) #1 row, 2 columns, 2nd plot
# plt.ylim(0,140000) #set y-axis limits within each subplot
# plt.plot(mySamples, myExponential, 'r', label = 'exponential', linewidth = 5.0) #red dashed line
# plt.legend()
# plt.title('Cubic vs Exponential')
# plt.show() #notice overlaps are not desired, so set limits

# plt.figure('cube exp log')
# plt.clf() #clear the frame
# plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 2.0) #green triangles
# plt.plot(mySamples, myExponential, 'r', label = 'exponential', linewidth = 4.0) #red dashed line
# plt.yscale('log') #logarithmic scale
# plt.legend()
# plt.title('Cubic vs Exponential')

# plt.figure('cube exp linear')
# plt.clf() #clear the frame
# plt.plot(mySamples, myCubic, 'g--', label = 'cubic', linewidth = 2.0) #green triangles
# plt.plot(mySamples, myExponential, 'r', label = 'exponential', linewidth = 4.0) #red dashed line
# plt.legend()
# plt.title('Cubic vs Exponential')
# plt.show() #notice the difference

#EXAMPLE: Retirements Savings -- Compound Interest
# save m each month, invest at r annual interest rate, retire with goal g

# #Assumptions:
# #annual salary: 100,000
# #monthly salary: 100,000/12
# #save 10% of salary each month
# #annual return on investment: 5%
# #goal: 1,000,000

def retire(monthly, rate, terms):
    """
    lists of savings and base to start
    monthly: amount saved each month
    rate: annual interest rate
    terms: number of months
    
    returns: lists of base and savings
    """
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i] #next label for next month
        savings += [savings[-1]*( 1 + mRate) + monthly] #add to updated value savings, add the monthly savings
    return base, savings #x and y labels

def displayRetireWMonthlies(monthlies, rate, terms):
    """
    """
    plt.figure('retireMonth')
    plt.clf() #clear the frame
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label = 'retire: €' + str(monthly))
        plt.legend()
    plt.show()

def displayRetireWRates(month, rates, terms):
    """
    """
    plt.figure('retireRate')
    plt.clf() #clear the frame
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label = 'retire: €' + str(month) + ' @ ' + str(int(rate*100)) + '%')
        plt.legend()
    plt.show()

def displayRetireWMonthsRates(monthlies, rates, terms):
    """
    """
    plt.figure('retireMonthRate')
    plt.clf() #clear the frame
    plt.xlim(30*12, 40*12) #set x-axis limits or look at range of terms
    for monthly in monthlies:
        for rate in rates:
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, label = 'retire: €' + str(monthly) + ' @ ' + str(int(rate*100)) + '%')
            plt.legend()
    plt.show()

displayRetireWMonthlies([90, 200, 500, 750, 1000], 0.05, 25*12)

# displayRetireWRates(500, [0.03, 0.05, 0.07], 25*12)

# displayRetireWMonthsRates([500, 700, 900, 1100], [0.03, 0.05, 0.07], 40*12)
#too much overlay, can change the scale to clarify the differences or be more careful

def displayRetireWMonthsAndRates(monthlies, rates, terms):
    """
    """
    plt.figure('retireMonthRate')
    plt.clf() #clear the frame
    plt.xlim(30*12, 40*12) #set x-axis limits or look at range of terms
    monthLabels = ['r', 'b', 'g', 'k'] #create set of labels for months
    rateLabels = ['-', 'o', '--'] #create set of labels for rates
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]#pick new label for each month
        #so it's going to cleverly walk through the list of labels
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]#same trick; new label each rate
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, monthLabel + rateLabel, label = 'retire: €' + str(monthly) + ' @ ' + str(int(rate*100)) + '%')
            #putting both labels together for plot
            plt.legend()
    plt.show()

# displayRetireWMonthsAndRates([500, 700, 900, 1100], [0.03, 0.05, 0.07], 40*12)
#color says the monthly savings and the style gives the interest rate/growth

#easier seeing grouping of plots
#interaction with plotting routines and computations allows you to explore the data:
#change display range to focus on areas of interest (eg last 10 years)
#change sets of values and vizualize effects (eg looking at different rates and savings)
#change display parameters to highlight clustering of plots by parameter