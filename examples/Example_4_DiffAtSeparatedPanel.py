from splot.splot import data_dict, Splot, c
import numpy as np

############################################################################
# A plot for multiple meas, cal and diff at top panel
# The diff curves are generated by the splot
# the diff curves are also plotted at the bottom panel
#########################################################################

#plot axis setup: 2 rows 1 column
myplot = Splot(2,1)

r = [0, 20, 50, 80, 100]
for i in r:
    # load the data:
    dataPath = "data/4/" + str(i)
    r = np.loadtxt(dataPath, skiprows=4, usecols=(0,))
    gtrunc = np.loadtxt(dataPath, skiprows=4, usecols=(1,))
    gcalc = np.loadtxt(dataPath, skiprows=4, usecols=(3,))

    # Set up data: G -- Measure data, Gcal -- Calcauted data
    G = data_dict((r, gtrunc), samplename="Ag", scan=str(i),
                  marker='o', color=c[i // 10 + 1])
    Gcalc = data_dict((r, gcalc), color=c[5], scan='Calculated')

    # plot data: y offset is set to the number of the file name
    myplot.plot_data(**G, offsety=i)

    # plot calculated curve at the same position, add outside legend
    myplot.plot_data(**Gcalc, offsety=i, diff=True, legend='out')

    # plot the diff curve at bottom panel(0,1): 2 steps
    # 1. load the G and Gcalc to the pannel
    myplot.add_data(G['data'], 1, 0)
    myplot.add_data(Gcalc['data'], 1, 0)
    # 2. plot the diff only
    myplot.diff_c(1, 0, offsety=i // 10)

    # reset the panel at both panels for replotting another set of G and Gcalc
    myplot.clear_data(0, 0)
    myplot.clear_data(1, 0)

# Resize the figure to be taller
myplot.figure_size(4, 8)

# Show figure and save
# myplot.show()
myplot.save(name='Example_4_DiffAtSeparatedPanel', form='pdf')