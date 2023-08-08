# git_assignment_HeroVired
## CalculatorPlus App
### In this Question we create a python programm for arithematic operations simultaneously in two branches and merge them into main branches and release it as versions of App
#### *branch 1 DEV*
- In this branch we write the code for ADD,SUBTRACT,MULTIPLY,DIVIDE functions.
- Then merge the code into main branch as version 1 and release the version1 code 
#### *branch 2 feature/sqrt*
- Then create a feature/sqrt branch fetch the code from origin by using *git fetch --all* command and add the sqrtcode to the abov code . - Here I observe there is bug in dev branch . 
- Then I checkout into dev branch and modify the code.Then again merge the code into main.
- Then checkout into feature/sqrt branch keep it up to date then check the working of code correctly. 
- Then i push the code into feature/sqrt branch .
- Then create a pull request to merge into dev .
- Here i add a collabrator to check the sqrt branch code for any errors/bugs.
-  After He approves the code i merge it into dev branch.
#### TEST using pytest
Finally do the testing in the 'dev' branch and create a CSV file . merge the both csv file and code into dev brance and release the **version 2** of the app

## Git LFS
### In this Question we add the binary file which is more than 200MB into git and check the file will be downolad on another machine correctly  
#### First we need to install git lfs in our system for this :
- create a lfs branch in same directory and add the binary file in the folder then do the following activity in lfs branch
#### git lfs install
#### git lfs track filename
#### git add filename
#### git commit -m "lfs commit"
#### git push --set-upstream origin lfs 

- After push the file clone the repository on another machine to verify that the binary files are download correctly



## Geometry-calculator 
#### In the Question we write a python code related to circle and rectangle area in two simulataneous branches using STASH command and merge them into dev and then  finally into  main branch.
- Create a new branch named "feature/circle-area" to work on the circle-area feature
- Before committing the changes, stash them using git stash to save the incomplete feature implementation.
- Verify that the working directory is clean
- Create a new branch named "feature/rectangle-area" to work on the rectangle area
- Before committing the changes, stash them using git stash to save the incomplete feature implementation.
- Verify that the working directory is clea
- Switch back to the "feature/circle-area" branch to continue working on the circle area feature.
- Retrieve the stashed changes
- Complete the circle area feature implementation and save the changes.
-  Switch back to the "feature/rectangle-area" branch to continue working on the rectangle area feature.
- Retrieve the stashed changes
- Complete the rectangle area feature implementation and save the changes.
- Create a pull request to the ‘dev’ branch.
- Have another team member or reviewer review your pull requests.
- After receiving approval, merge both pull requests into the main branch
