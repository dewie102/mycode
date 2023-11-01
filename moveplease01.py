#!/usr/bin/env python3

# Standard library imports
import shutil # Shell utilities will be used to move files
import os # Provides access to low level os operations

def main():

    os.chdir('/home/student/mycode/') # Move into this working directory
    shutil.move('raynor.obj', 'ceph_storage/') # Try moving the file raynor.obj into ceph_storage/ dir

    # Program will pause while we accept input
    xname = input('What is the new name for kerrigan.obj? ') # Collect string input from the user
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # Moving kerrigan.obj into ceph_storage/ with new name

if __name__ == "__main__":
    main() # This calls our main function
