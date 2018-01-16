Quickstart User Guide
======================
The Quickstart Guide provides you the most basics to get start with Splot software. It covers a brief overview of what the Splot is, followed by a most general procedure to install and use Splot, then a few examples in the end. You can copy and paste the code to make the desired scientific figures.

Note:
 To report issues, post your problems/questions to `Splot Issues <https://github.com/Billingegroup/splot/issues>`_. You are also welcome to put feedback here to help us improve the software. 

Overview
--------
The splot software is developed for the Billinggroup members to make 
quick scientific plots with Billinge group style. It is especially easy to use when plot measured G(r) data together with the fitting curve and the difference curve. Other features of the group style figure includes well configured compact multi-panel, nice color selection and carefully chose line thickness or marker size for high quality figures for papers. The figure may not look good when you generate, but will look nice when you put in your paper. Try it!

Getting Start
-------------
**Installation**

1. Open Terminal (for Mac) or Command Prompt. 
2. Set up conda environment.
    - If you haven't had a conda environment:
       - Create one with deps `conda create -n splot python=3 billingegroup -c conda-forge`
       - Activate the environment you created with `source activate <env_name>`
    - If you have conda environment already installed: 
       - Make sure you have installed the billingegroup package. If you haven't, install with `conda install billingegroup`
       - `source activate <your conda environment name>`
3. Change the current working directory to the location where you want the cloned directory to be made. 
4. Copy and past this code to your command line `git clone https://github.com/Billingegroup/splot.git`
5. Install splot with `python setup.py develop`. Now the installation is completed.

**General procedure to make a plot in 8 steps**

You can use the examples provided in the "examples" folder as templates to start, if you find any provided demo looks similar to your desired plot. Copy the code then customize to meet your own needs may be quicker in this case. 

The following guide will demonstrate how to create a plot from scratch. 

1. Import splot with `from splot import data_dict, Splot`. In case you want to choose colors yourself instead of using the default color by the splot, you can also import the Billinge Group color collection by adding the `bgcolor` in the import line. 

2. Get your data into Splot : create data dictionaries. The Splot only recognizes data dictionaries, not data arrays, to make plots. So you need to prepare your data to be in the form of a dictionary before plotting. Hint: make as many data dictionaries as you would plot.
    - Find your path to where your data files being saved. You can use a string variable to store this path. 
      ```
      Example: 
      dataPath = your data direcotry path
      ```
    - Generate a dictionary for this data file by calling the data_dict function. Parameters for this function includes: the data path you created in step 1, the sample name and scan name for your data. 
      ```
      Example: 
      mydata = data_dict(dataPath, samplename=your sample name, scan=your scan name)
      ```
    - For further customization, which innecessary in most cases, you can pass in the parameters used by matplotlib for the plotting style.
      ```
      Example: 
      mydata = data_dict(dataPath, samplename=your sample name, scan=your scan name, marker='o', linestyle='--')
      ```
      The last two arguments, the marker='o' and the linestyle = '--', will plot your measured data as circle connected by a dashed line. Again, the syntax is same as that used in matplotlib. You can check to the matplotlib for a comprehensive list. 
    - That's all the pre-plotting work. Now let's plot them!
3. Make a plotting grid by calling Splot() and providing it with the dimensions of your grid, `Splot(the number of rows, the number of columns)`. Don't forget to give a name for your plot. For demonstration, let's use a name 'myplot' in all the following examples. 
   ```
   A grid of 2 rows by 1 columnm:
   myplot = Splot(2, 1)
   
   A gird of 3 rows by 2 columns:
   myplot = Splot(3, 2)
   
   One single panel, leave the dimensions empty:
   myplot = Splot()
   ```

   *Please Note: this step has made a splot instant which be referred by the name you gave for this specific plot, in our demonstration, myplot. From now on, you can call all the methods (functions) written in the Splot class by `myplot.methods(argumets)`.*
   
4. Plot your data with the plot_data() method. 
   - The plot_data() plots the measured data. If there are calculated data and the diff curve in you data file - the one you used to make a data dictionary - this method can plot them with your measured data together. To enable this function, you need to set the calc and diff parameters to be True. For more plotting tricks, please go to the Tips section.
   - For the multi-panel case, the panel position is controled by the parameters r and c in plot_data(). They refer to the numer of row and column on the gid. Splot uses zero-based index, so you count from 0 instead of 1. 
   ```
   Quick Examples
   
   To plot mydata, the data dictionary you had created in step 2, 
   at panel (3, 1) on a 3x2 multi-panel gid: 
   myplot.plot_data(**mydata, r=2, c=0)
   
   To include the Calculated curve at the same panel:
   myplot.plot_data(**mydata, r=2, c=0, calc=True)
   
   To include the Calculated curve and Diff curve at the same panel: 
   myplot.plot_data(**mydata, r=2, c=0, calc=True, diff=True)

   Scale your data by a factor of 1.5 in the plot: 
   (this will also scale your calcualted curve by the same amount) 
   myplot.plot_data(**mydata, r=2, c=0, calc=True, diff=True, 
   					scale = 1.5)
   
   Shift your data on x by a unit of -6, and a unit of 12 on y-axis:
   (the calcualted curve and diff curve will be shifted too)
   myplot.plot_data(**mydata, r=2, c=0, calc=True, diff=True, 
   				    offsetx=-6, offsety=10)
   
   Shift the diff curve 10 unites below your measured (or calculated):
   myplot.plot_data(**mydata, r=2, c=0, calc=True, diff=True, 
   					diffoffset=-10)
   
   Reminder: Please don't forget the two asterisks associated 
   with the data dictionary. 
   ```
5. An optional step: after you complete the plot at all panels, you can adjust the addjust the plotting range. The set_xlim() and set_ylim() methods allow to change the plotting range for entire column or row, because the compact panel shares x range at the same column, and shares y range at the same row. The first parameter is the position of the col or row, again, we count from 0. 
   ```
   Set the x range for the first column to be -10 to 40:
   myplot.set_xlim(0, -10, 40)
   
   Set the y range for the second row to be -15 to 35:
   myplot.set_ylim(1, -15, 35)
   ```
6. Configure the plot by the config() method. This is a must step. However, with the config() method, you can chose to make the plot for in paper, or presentation (to be continued), or manually set the position of the legend, add your own title and label. 
   ```
   Most of the case, for a G(r) plot, you can leave the parameters blank:
   myplot.config()
  
   For manuscripture, use the context parameter:
   myplot.config(context='manu')
   
   Add a title 'My Plot':
   myplot.config(title = 'My Plot')
   
   Place the legend outside of the plot:
   myplot.config(legend = 'out')
   
   Make the x and y labels:
   (if you don't write them in math text, rememerb to turn off the math) 
   myplot.config(x='distance', xunit='meter', y='Force', yunit='N',
   				label_math = False)
   ```
  
7. See your figure in a GUI window by `myplot.show()`.
8. Save your figure by save method. Don't forget to give the name in saving your plot. You can also change the format to be pdf, eps, etc.  `myplot.save(name="myplot", form="eps")`.  

###### Misison Complete! The above examples have covered the basic functionality for a quick plot as Billinge Group Standard. In general, you can read Splot Class to try more functionalities. For creative uses, here are some tips you might try. 

### Tips
--------
 -  *The position of diff curve*: The diffoffset parater in plot_data() is the reference location of the diff curve to the measured / calculated curve. Splot has set a fixed amount distance. When you don't need this seperation, but want its original position as it is stored in your data file, you can set the diffoffset = 0 in the plot_data(). 
 -  *Plot the diff curve at a different panel than the measured / calculated data*: The Example_4_DiffAtSeparatedPanel can be a reference.
 	-  You still need to plot the measured data before procedding the following. The reason to do this is so that the splot can register the data dictionary where the diff curve comes from, and associate this diff curve to the labels. 
 	-  Now assume you have plotted the measured somewhere on your grid, to plot the diff curve at a different panel, you can turn off the measured data and turn on the diff curve. Remember, you can always set the position of the diff curve in the parameter diffoffset. 
 	```
    Example: 
    myplot.plot_data(**mydata, meas = Flase, diff = True, diffoffset=0)
    ``` 
 - *Use Splot to plot a curve difference between any two data sets :* the curves_diff() method. This function can plot the difference betwee: 1. the two measured data; 2. between the two calculated data; 3. between the two diff curves. For details please read the doc string of the curves_diff(). The which_diff parameter gives you the options for this. 
    ```
    Example 1 
    plot the difference curve between two measured data at panel(1,1)
    myplot.curves_diff(data_dictionary1, data_dictionary2, r=1, c=1). 
    
    If you want to make the label visible:
    myplot.config(context='')
    
    Example 2 
    plot the difference curve between two calculated data at panel(1,1)
    (This assumes that you have the calculated data in your data file.)
    You can use scale, offsety, matplotlib plotting style for this curve.
    myplot.curves_diff(data_dictionary1, data_dictionary2, r=1, c=1, 
    					which_diff='Calc', scale = 3.5, offsety = 0, 
                        linestyle = '--'). 
                        
    Example_2_MeasCompare can be a reference as well. 
    ```
 
 - *Resize your figure* by `myplot.figure_size(width, height)`
 -------------
 #### End
