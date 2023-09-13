# "Introduction to scientific programming" @ Med Uni Graz

Dear participant, 

welcome to the course of Introduction to scientific programming. We are very happy to offer this year a first course about programming within the PhD School MolMed. In this course, we will get the basics in two of the main lenguages used in Science: python and R. We will also introduce how to work under Linux environment, the use of some command in the terminal (bash) as well as how to submit jobs to a scientific cluster using the job manager SLURM. 

The course will take place the week Nov. 6-10 2023 at the Med Campus in the room SR58 (MC2.Q.01.033).


# 1. Linux environemnt, bash and HPC

# 2. python
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


