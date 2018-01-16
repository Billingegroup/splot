# splot v.01
This pacakge contains plotting tools for quick generating Billinge Group standard figures.  
Splot makes 2D plots of data on compact multi-panel.  
It's designed for easy plotting measured, calculated data, and difference curve.  

# Platform: 
Linux, Mac, Windows  

# Release data: 1/23/2018  

# Intended Audience
Billinge Group members

# Installation
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

# Usage
See the QuickstartUserGuide.md.
