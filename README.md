# Introduction to scientific programming @ Med Uni Graz

Dear participant, 

welcome to the course of Introduction to scientific programming. We are very happy to offer this year a first course about programming within the PhD School MolMed. In this course, we will get the basics in two of the main lenguages used in Science: python and R. We will also introduce how to work under Linux environment, the use of some command in the terminal (bash) as well as how to submit jobs to a scientific cluster using the job manager SLURM. 

The course will take place the week Nov. 6-10 2023 at the Med Campus in the **room SR68 (MC2.Q.01.040) (NEW ROOM)**.


# 1. Linux environement, bash and HPC

## 1.1. Installation and previous requirements
We have prepared a virtual machine with Debian for the course to be used on the laptops of the PC Pool. We will cover the following topics:

## 1.2. Content

- Introduction to Linux environment, distributions, permissions
- Command-line basics
- Vi editor
- Environment variables, .bashrc file
- Scripts and running scientific jobs
- Visualization of data with gnuplot
- SLURM

# 2. python
## 2.1. Installation and previous requirements

## 2.2. Content

**(1) BASIC PYTHON**

1. wwwPython (What? Why? Who?)
2. Installation and usage
    2.1 Install python
    2.2 How to write/run a python script

3. Data Types and Structures

    3.1 Basics data types

    3.2 Basics data structures

4. Conditionals and Loops

    4.1 if/else/elif

    4.2 for/while loops

5. Code reuse

    5.1 Functions

    5.2 Import


**(2) PANDAS**

INTRODUCTION: 
	- installing pandas
	- pandas series
	- pandas DataFrame
	- reading data from a file
	- viewing data (head, tail, shape, info, list column names)
	- outputting files

DATA CLEANING:
	- missing values (check, count, remove)
	- duplicates
	- rename columns
	- add/remove columns and/or rows (drop, iloc, loc)
	- strip function

DATA MANIPULATION:
	- selection operation 
	- data transformation (categorical variables)
	- standardizing/formatting column values using replace
	- standardizing/formatting phone numbers (replace, apply functions)
	- splitting columns
	- filtering down rows of data
	- groupby function

MULTIPLE DATAFRAMES:
	- concatanting two dataframes
	- merge function (merging based on a mutual column)

resources:
- https://www.youtube.com/watch?v=CIQJtJ38-hI
- https://www.youtube.com/watch?v=bDhvCp3_lYw
- https://www.datacamp.com/tutorial/pandas
- https://coursera.pxf.io/BXY3Wy
- https://bit.ly/3KHMLlu
- https://leetcode.com/studyplan/30-days-of-pandas/

**(3) MATPLOTLIB**

1. Basic plotting with Matplotlib
- creating a simple line plot
- adding labels and titles, legends, grids
- customizing colours and styles
- saving plots to files
2. Different types of plots
- scatter, bars, histograms, pie charts
3. A few exercises where students apply their Pandas knowledge to plot data from files

# 3. R 

## 3.1. Installation and previous requirements

Install and prepare software needed: 

### Download R from CRAN (comprehensive R archive network)
https://cloud.r-project.org
You will find links to the download depending on your operating system (Linux, macOS, Windows). There are regular releases, i.e., update regularly.


## RStudio
RStudio is an integrated development environment (IDE) for R programming and can be downloaded:

https://posit.co/download/rstudio-desktop

The download for Windows is very prominent on the webpage, however, you will find the download file depending on your operating system (Linux, macOS, Windows) listed further down on the webpage, i.e. scroll down.

Also RStudio is updated on a regular basis, i.e. check for updates. 

#### R packages and updates
1.	Open RStudio
R will be now automatically running within the RStudio environment. The following figure shows how RStudio is structured (source: https://docs.posit.co/ide/user/ide/get-started/)

<img width="241" alt="image" src="https://github.com/CAMDgraz/intro_programming/assets/75629351/16ce58dc-76e6-4994-a819-6bdc65689949">

 
3.	Install R packages
Copy & paste the following statement in the command window

install.packages(c('tidyverse','ggplot2','knitr','gtsummary','flextable','openxlsx','readxl','xlsx','nlme','lme4'))

This will install the following R packages
•	tidyverse
•	ggplot2
•	knitr
•	gtsummary
•	flextable
•	openxlsx
•	readxl
•	xlsx
•	nlme
•	lme4

3.	Update R packages
Copy & paste the following statement in the command window

update.packages(ask = FALSE)

This will update all R packages which come with the installation of R. Please be aware that also R packages are updated on a regular basis, i.e. check for updates.


