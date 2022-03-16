# Frequently asked questions

The [contributing guide](CONTRIBUTING.md) outlines the basic steps of starting contributing to the CSC user guide, making pull requests (PRs) and reviewing them. This page highlights in more detail common questions and pitfalls you may encounter during the process.

## My PR did not pass the tests, what to do?

Tests are run to check, for example, that your pull request complies with the CSC Docs style guide and that there are no broken links. If any such errors are found in your commits, the tests will not pass and you need to figure out what went wrong:

1. Find out which tests did not pass under the notification `Some checks were not successful` in the Review-dialogue (marked with a red x and text `Failing after X - Build Failed`).
2. To the right of the failed test, click `Details`, which opens the `Checks` tab.
3. Under the `Build Failed` section, click the link at `The build failed` to open the Travis CI page with logged details on the build.
4. Scan through the Job log for any text marked in red. These are errors that the test found, and the reason for them is written before the red text. 
5. An example error is shown below. Here, the `link_check.py` test script was run to see whether any links were broken. The test found two broken section links and it tells you in which files and on which lines the errors are.

```console
$ python3 tests/python_link_tests/link_check.py
The section link namd.md#batch-script-example-for-mahti in file docs/apps/namd.md on line 33 is broken
The section link cp2k.md#example-batch-script-for-mahti-using-mixed-mpi-openmp-parallelization in file docs/apps/cp2k.md on line 81 is broken
No broken file links found
No hidden files found
The command "python3 tests/python_link_tests/link_check.py" exited with 1.
```

6. Fix the links and commit the revised files to the same branch and the tests should now pass.

## How to edit an existing page on CSC Docs?

## How to create a new page to CSC Docs?

## How can I preview my edits?