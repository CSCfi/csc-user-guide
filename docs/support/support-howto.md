---
description: Things to include in your CSC servicedesk support request
---

# How to write good support requests

Writing a good support request will enable us to resolve your issue faster. Below is a list of good practices.

## Specify your environment

On which system are running? Have you or your colleague compiled the code? Which modules were loaded? If you use non-default modules or e.g. Conda environments and you do not tell us about it, time will be wasted when we try to debug your issue in a different environment.

## Include actual commands and error messages

We cover this below, but it’s so important it needs to be mentioned at the top, too: include the actual commands you run and the actual error messages (also Slurm error and output). Copy and paste.

## Give a descriptive subject

Your subject line should be descriptive. "Problem on Mahti" is not a good subject line since it could be valid for many of the support emails we get. The support staff is a team. The subjects are the first thing that we see and a good subject will speed up the issue going to the right specialist.

## Be specific

Whatever you do, don’t say that “X didn’t work”. Give the exact commands you ran, environment (see above), and output error messages. The actual error messages mean a lot - include all the output, it is easy to copy and paste it.

The better you describe the problem the less we have to guess and ask. Make the problem reproducible. See also next point.

## Tell us which documentation you have already read

If you are asking for advice on e.g. how to use a particular software package, then please explain in detail what documentation you have already read and why this hasn't yet fully answered your question. This allows us to answer your specific question instead of simply referring you to the existing documentation.

## Send your requests to ServiceDesk

Always send requests to [CSC Service Desk](contact.md) instead of staff members directly. In the Service Desk they get tracked, have higher visibility and will get picked up by the correct specialist. Some staff members work for the support requests only part time and we are also on holiday sometimes.

## Tell us also what worked

Rather often we get requests of the type "I cannot get X to run on two nodes". The request then does not mention whether it worked on one node or on one core or whether it never worked and that this was the first attempt. Perhaps the problem has even nothing to do with one or two nodes. In order to better isolate the problem and avoid losing time with many back and forth emails, please tell us what actually worked so far. Tell us how you have tried to isolate the problem. This requires some effort from you but it will help us to resolve your issue faster.

## Identify yourself

Give your CSC username and professional affiliation (if using non-professional email account like gmail).

## New problem, new email

Please do not send support requests by replying to old tickets, which probably concern unrelated issues. Every issue gets a number and this is the number that you see in the subject line.

## The XY problem

This is a classic problem. Please read [more about the XY problem here](https://xyproblem.info/). Often we know the solution but sometimes we don't know the problem.

In short (quoting from the previous website):

*   User wants to do X.
*   User doesn't know how to do X, but thinks it can be done via Y.
*   User doesn't know how to do Y either.
*   User asks for help with Y.
*   Others try to help user with Y, but are confused because Y seems like a strange problem to want to solve.
*   Finally, the issue is solved by doing X without Y.

To avoid the XY problem, if you struggle with Y but really what you are after is X, please also tell us about X. Tell us what you really want to achieve. Solving Y can take a long time.

## Create an example which reproduces the problem

Create an example that we can ideally just copy/paste and run and which demonstrates the problem. It is otherwise very time consuming if the support team needs to write input files and run scripts based on your possibly incomplete description. See also next point. Make this example available to us. We do not search and read read-protected files without your permission (and only very few even can).

## Make the example as small and fast as possible

You run a calculation which crashes after running for one week. You are tempted to write to support right away with this example but this is not a good idea. Before you send a support request with this example, first try to reduce it. Possibly and probably the crash can be reproduced with a much smaller example (smaller system size or grid or basis set). It is much easier to schedule and debug a problem which crashes after a few seconds compared to a run which crashes after hours. Of course this requires some effort from you but this will help us to resolve your issue faster. Often when isolating the problem, the problem and solution crystallize before even writing the support request.

## If you can't create an example, explain what you've done

Explain the steps and commands you've given before the problem and all output and errors that are produced. If the amount of data is large (more than 1MB) you can use [FUNET FileSender](https://filesender.funet.fi/) or [a-flip](../data/Allas/using_allas/a_commands.md#a-flip) to deliver files. Be specific, see above.

[_"How to" reused by permission from HPC group - UiT The Arctic University of Norway._](https://hpc-uit.readthedocs.io/en/latest/help/writing-support-requests.html)
