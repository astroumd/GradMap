# Practical Git for GradMap

If it works for you, a fresh version of the *GradMap*
material can be obtained with the command

    git clone https://github.com/astroumd/GradMap

this will create a new directory *GradMap/* in the directory where
you issued this command. You can then skip the next section on how
to install git. If you just want to use the material, you will also
not need a github account. You can then stop reading here.

The url on github is :    https://github.com/astroumd/GradMap

A typical terminal session to add/modify code is:

    cd GradMap                 # change directory someWhere
    git pull                   # be sure to update your local repo
    git add some_File          # (if need) tell git there is a new file
    git commit some_File       # add it to the local repo (+ log entry!!)
    git push                   # push everything to the remote repo

Special caution for **ipynb** notebooks: make sure you have
have cleared the cells via **Kernel->Restart & Clear Output**
before saving them in git.

Also note we are using python3, if you open the **notebooks/example-python3.ipynb**
you should not get any warnings about missing python kernels, or more than likely
you happen to use python2.

## 0. VCS


VCS = Version Control System.

Examples are :   RCS, CVS, SVN, Mercurial (gh) and GIT

## 1. Installing git

In order to access the GradMap material, you will need a git client. There
are command line and GUI versions of git. You can go out and hunt for one
via google, or ask your best friend, or follow this document.


### 1.1 Command Line Git

The terminal/shell should have a command "git".  OSX now comes
preinstalled with this. If your linux distribution does not have git
by default, simply install it. On a Debian based Ubuntu linux this would be

     sudo apt-get install git
     
or on a RedHat based linux you would probably need

     sudo yum install git


### 1.2 Graphical Interface Git

Since we are using [GitHub](https://github.com), 
the [GitHub Desktop](https://desktop.github.com/) may be the most natural
choice for a graphical client. It only works on Windows and OSX


For linux **gitk** and **gitg** are excellent choices. They are available on most
major linux distros.

Here is a more complete listing with some screenshots: https://git-scm.com/downloads/guis


## 2. Get a github.com account

If you want to contribute to the development of **GradMap**, you will need to
create an account on https://github.com

## 3 clone or fork?

If you want to contribute to GradMap you have two options:

### 3.1 "clone"

This is the most simple (but also a bit dangerous) method.
As was mentioned in the beginning of the document, you make a clone of the
repo:

     git clone https://github.com/astroumd/GradMap


### 3.2 "fork"

We will probably not be using this method, and allow direct push into the repo.

For this you need a github account. On https://github.com/astroumd/GradMap
you would click on the "Fork" button near the top right., and that creates
a clone of this repo under your personal account. So, lets say for the
user teuben I then have a fork on https://github.com/teuben/GradMap. You
can now continue on the "clone" option, but use your personal repo:

     git clone https://github.com/teuben/GradMap

after this you would need to create a branch, work on the branch, push this
to your github account, and submit a pull request from that branch. Sounds
complicated? yes!  But this is how it's done in most open source projects.


## 4. Editing

Here is a sample terminal session, editing a file, and returning that changed
file to the remote repo.

     cd GradMap/docs             ### change directory "anywhere" in the repo
     git status                  #   see if there are any loose ends
     git pull                    ##  pull in work from others
     edit git.md                 ### edit some file
     git status                  #   check status
     git commit git.md           ### commit to your local repo
     git push                    ### copy all commit's to the remote repo


## 5. Configuring git

I find some of the default settings in git a bit annoying. The command

    git config --list

will list your git settings (on unix, see also the **~/.gitconfig** file, which you
can also edit directly if you know what you are doing). Here are some of my favorite
settings and aliases:

    git config --global user.email          "teuben@gmail.com"
    git config --global user.name           "Peter Teuben"
    git config --global alias.ci            "commit"
    git config --global alias.co            "checkout"
    git config --global alias.st            "status"
    git config --global credential.helper   "cache --timeout 100000"

Notice git has not only global settings, but can be overridden by setting per repo (as defined
when your working directory is somewhere within that repo) by leaving off the '--global' option.

## 6. Other git trivia

* Inline help:
  * git
  * git help CMD
  * git CMD --help
* never touch the .git directory at the top of a repository (this is your local repo history)
* git commands you should know for GradMap
  * **git clone**    (first time only)
  * **git pull**     (update from remote)
  * **git push**     (update to remote)
  * **git status**   (what's new)
  * **git add**      (new files)
  * **git commit**   (local write)
  * **git log**      (logs of who did what)

## 7. Overview
![git overview](Git_operations.svg "git operations overview")

(taken from WikiMedia)

# Old Material That Will Be Removed 

1) Direct push/pull
    

This is dangerous, needs special permission from the owner
but is a very simple sequency of commands, and not too different
for those used to CVS and SVN

    	git clone https://github.com/astroumd/demo  demo_astroumd
        cd demo_astroumd
        $EDITOR f1
        git commit f1
        git push

   This is the typical work if you work on your own repo.

2) A variation on this theme is using a branch, so they could be more safely
   merged into the master. So, instead of editing 'f1' in the master, we
   create a branch and make changes on that:


   	git branch b1
	git checkout b1
	$EDITOR f1
	git commit f1
	git push                   # skip this if you want it only local

   When it comes time to merge, the following sequence can be followed

   	git checkout master        # start from a fresh master
	git pull
	git merge b1               # merge in the b1 changes, watch for conflicts
	git push                   # push this back to github


3) fork the master in your own GITHUB workspace, clone from that to your laptop,
   work on a branch, and go a pull request on GITHUB from that branch, viz.
   (below your name on GITHUB is "gh_name")

   	1) go on GITHUB and fork the repo to your space
	   (see the fork button top right)
	   
	   https://github.com/astroumd/demo


	2) now on your laptop get your own version (as "teuben") where you edit
	   on the branch

	   git clone https://github.com/teuben/demo demo_teuben
	   cd demo_teuben
	   git branch b1
	   git checkout b1 
	   git branch               # shows you all branch names
	   git branch -r            # shows all branches on (my) remote
	   $EDITOR f1
	   git status
	   git commit f1
	   git push -u origin b1    # push it back to your GITHUB


	3) now go back to your GITHUB.COM space, and pick your "b1" branch,
	   and issue a PULL REQUEST
	   Wait for an email when this was merged by the coordinater
	   When this is done, your b1 branch was merged into the master
	   
	   On GITHUB you can do that pull request merge graphically, but they also
	   show you the command line sequence: (untested)
	   	# put teuben's branch into your repo
	   	git checkout -b teuben-b1 master
		git pull https://github.com/teuben/demo.git b1
		# merge those changes and push back onto github
		git checkout b1
		git merge --no-ff teuben-b1
		git push origin b1

        4) Fetch the new master now from the original provider, which we'll label as "upstream"

	   git remote                                                   # see which ones you have
	   git remote add upstream https://github.com/astroumd/demo     # add this if you don't have it

	   git checkout master                                          # make sure you're on your master
	   git fetch upstream                                           # fetch it
	   git merge upstream/master                                    # merge in 
	   git status                                                   # there should be no new things
	   git push                                                     # push it to your origin


         5) If you really don't care about that branch "b1" anymore, it can be deleted.

           git checkout master
	   git branch -D b1
	   git push origin --delete b1

The 'astropy' project has a nice writeup about their workflow:

http://docs.astropy.org/en/stable/development/workflow/development_workflow.html

