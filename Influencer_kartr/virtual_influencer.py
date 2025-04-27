# Install the required version of pyttsx3
!pip install pyttsx3==2.91.2
!pip install pygit2==1.12.2

# Change directory to /content
%cd /content

# (No need to clone anymore)

# Change into the Fooocus directory (local path)
%cd Fooocus-main/Fooocus-main

# Run the entry_with_update.py script with the --share flag
!python entry_with_update.py --share
