# git start 

## Date: 2018-07-10

## Index 
- What is git? 
- Who can do this? 


### What is git?

Git is blahblah 

### Who can do this? 

Anyone.

## Date: 2019-02-02 

Shell command & Git 

cd : To the top directory 
cp : copy 
cp (folder_name) (copied_name) 
Overwritten if there is a duplicate 
mv : Move files ; rename files 
rm : remove files
rm -r : Recursive file erase including the directory
mkdir: Make directories 
echo : print 
pwd : print working directory 
cat: view file content
less: Display one page 
	- press spacebar to page down 
	- “q” to quit 
	- “:n” move to next file
	- “:p” go back to previous file 
	- “:q” to quit 
head: Only print out the first few lines of file
history: Print a list of commands 
!(number) to rerun number-th command


chsh -s /bin/zsh: Change the shell to zsh 
chsh -s /bin/bash : To bash 


On the Linux Shell: 
Ctrl a : Move cursor to the beginning of line 
ctrl-e : move cursor to the end of the line 
ps -ax: list all the processes in the terminal 
ps -ax | grep <application name>


jupyter nbconvert  --to html [filename.ipynb] : Convert the file (notebook) into html 


jupyter notebook : Open jupyter notebook 

Git

git fetch : fetch the new update
git reset --hard origin/master 
git clone
Git workflow: 
Git init (the folder you want to initiate the git) 
Git add . (Get Git to track all files) 
git commit -m “some commit” (Update what have changed in the GitHub) 
Only once: git remote add origin/<branch> _____git url
git push origin master
