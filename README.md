# CyberGIS-Compute Hands-On Demo
In this example, we will show you how to add a manifest.json file to an already existing repo so it can run on cybergis-compute.

## Add manifest.json file
Easy as it sounds, add a manifest.json file to this repo. This will define how your project will run on the HPC. In this example, we will keep this as simple as possible, but for more reading, check out https://github.com/cybergis/cybergis-compute-hello-world/blob/main/README.md for a more in-depth example of information that can be added to the manifest file.

Add this to the manifest file:
```
"name": "hello world",
"container": "python",
"execution_stage": "python main.py"
```

## Contact Compute team
For security reasons, all the repos that can be run on Cyber-GIS compute must be verified by the Compute team. For this example, we have already verified your repo, but ordinarily you would need to reach out at this point in the process.

## Run your code!
Now, you can head over to CyberGISX to run your code. Check out https://cybergisx.cigi.illinois.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcybergis%2Fcybergis-compute-python-sdk&urlpath=tree%2Fcybergis-compute-python-sdk%2Fhello_world.ipynb&branch=v2 for an example of how to open the UI.
