Open OnDemand is a web interface for Puhti.
It can be used for creating and managing batch jobs, managing files, checking project status and quota usages and launching various interactive applications.

## Job composer
The Job Composer app is used for creating and managing batch jobs.
The [example batch job scripts for Puhti](../computing/running/creating-job-scripts-puhti.md) are provided as templates to copy from.
When you first launch the Job Composer app you will see a short tutorial.
After submitting the batch job using the Job Composer more information about the job can be found in the Active Jobs app.

## Interactive apps
Interactive apps are apps that can be launched and run on the compute nodes and provide a web interface.
These are apps such as Jupyter Notebook, RStudio, Visual Studio Code and Rclone.

If the interactive app does not start or does not work as expected you can delete the session and try to launch the app again.

### Launching an interactive app
The interactive apps can be found in the navigation bar or on `My Interactive Sessions` page.
After selecting an interactive app from the list you will be presented with a form to configure the session.
After submitting the app form the app will be started and you will be able to connect to the application on the `My Interactive Sessions` page.

### Jupyter
The Jupyter interactive app launches a Jupyter notebook that is accessible through the web interface.
Both Jupyter Notebook and Jupyter Lab with different Python environments are supported and can be selected in the form.

### Visual Studio Code
The Visual Studio Code interactive app can be used for editing and running code on Puhti.
Make sure to load the correct modules before launching the session for the debugger to work correctly.

Extensions can be installed in the extensions tab in VSCode. 
Dependencies for the extensions need to be loaded or installed for the extensions to work correctly.
E.g. the `go` module must be loaded before installing the `golang` extensions in VSCode.

### Rclone
Rclone lets you access files on Puhti and Allas in the web interface.
To be able to access files on Allas you need to configure the authentication for Allas.
That can be done by executing the following commands in Puhti.
```
module load allas
allas-conf -m s3cmd
```

