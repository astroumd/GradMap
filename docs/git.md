# Practical Git for GradMap

If it works for you, a fresh version of the *GradMap*
material can be obtained with the command

    git clone https://github.com/astroumd/GradMap

this will create a new directory *GradMap/* in the directory where
you issued this command. You can then skip the next section on how
to install git.


## 1. Installing git

In order to access the GradMap material, you will need a git client. There
are command line and GUI versions of git. You can go out and hunt for one
via google, or ask your best friend, or follow this document.


### 1.1 Command Line Git

The shell (even on Windows there is one) should have a command "git".
The mac now comes with this. If you linux distribution does not have
git, on a Debian based Ubuntu linux this would be

     sudo apt-get install git
     
or on a RedHat based linux you would need

     sudo yum install git

There are many ways to collaborate using git or in our case github
(skip to the last one if you don't care about the others)

### 1.2 Graphical Interface Git: windows



Since we are using [GitHub](https://github.com), 
the [GitHub Desktop](https://desktop.github.com/) may be the most natural
choice for a graphical client. It only works on Windows

### 1.3 Graphical Interface Git: mac

### 1.4 Graphical Interface Git: linux



## 2. Old 2Material

1) directly clone the owner's repo and push back into it.
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

