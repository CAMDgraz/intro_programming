# "Introduction to scientific programming" @ Med Uni Graz

Dear participant, 

welcome to the course of Introduction to scientific programming. 


# R 

Install and prepare software needed 
1.	Download and install R
2.	Download and install RStudio
3.	Install R packages listed below and update existing R packages
R
Download R from CRAN (comprehensive R archive network)
https://cloud.r-project.org. 
You will find links to the download depending on your operating system (Linux, macOS, Windows). There are regular releases, i.e., update regularly.
RStudio
RStudio is an integrated development environment (IDE) for R programming and can be downloaded
https://posit.co/download/rstudio-desktop/
The download for Windows is very prominent on the webpage, however, you will find the download file depending on your operating system (Linux, macOS, Windows) listed further down on the webpage, i.e. scroll down.

Also RStudio is updated on a regular basis, i.e. check for updates. 
R packages
1.	Open RStudio
R will be now automatically running within the RStudio environment. The following figure shows how RStudio is structured (source: https://docs.posit.co/ide/user/ide/get-started/):
 

2.	Install R packages
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

![image](https://github.com/CAMDgraz/intro_programming/assets/75629351/c6b33100-67db-4743-8a08-66c7e6ab27fc)
