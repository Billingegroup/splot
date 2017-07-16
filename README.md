# splot v.01
This pacakge contains plotting tools for quick generating Billinge Group standard figures.  
Splot makes 2D plots of data on compact multi-panel.  
It's designed for easy plotting measured, calculated data, and difference curve.  

# Platform: 
Linux, Mac  

# Release data: 7/13/2017  

# Intended Audience
Billinge Group members

# Installation
1.`git clone git@gitlab.thebillingegroup.com:analysis/17sx_plotting.git`  
2.
* If you have conda environment alreayd installed: 
  * Make sure you have installed the billingegroup package. If you haven't, install with `conda install billingegroup`
  * `source activate <your conda environment name>`   
* Else: 
  * Create a conda environment with deps `conda create -n splot python=3 billingegroup -c conda-forge`  
  * Activate the environment you created with `source activate <env_name>`

3.cd to the directory where you git cloned the 17sx_plotting  
4.Install splot by `python setup.py develop`  

# Usage
Note: beofre plotting, please generate a data dictionary with your data by the data_dict function provided in the splot module.  
The example directory under 17sx_plotting provides plotting example scripts. 