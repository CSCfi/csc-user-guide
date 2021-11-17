# Accessing Kvasi

You first need a CSC userid for Puhti. If you do not have one, check out the
[How to get started as a new user at CSC?](../support/faq/how-to-get-started-at-CSC.md) FAQ.

In order to access Kvasi, your CSC userid needs to part of the `kvasi-users` group. Send a mail to servicedesk@csc.fi and ask to be added to the **kvasi-users** group.

When you have been added, you can use SSH to login to kvasi.csc.fi directly. (Before August 2020, one had to go from/via Puhti, but not anymore)

## Setting up an SSH tunnel for the Jupyter web interface

In order to use the Jupyter notebook environment, you need to set up an SSH tunnel, forwarding the output port of your notebook environment to your local computer. Follow these steps:

1. Login to Kvasi with SSH:
    * `ssh <userid>@kvasi.csc.fi`
2. Start the Jupyter server: `./qlm_notebooks/launch_qlm_notebooks`. This will give you two values:
    * The Jupyter port number. It will be `8888`, or higher
    * The token for accessing the web interface (a string of letters and numbers)
    * Example output:

```
Jupyter port : 8888
Jupyter token: 123456abcdef

To access your Jupyter notebook from your local computer:

1. Create SSH tunnel:
    ssh -L 8890:localhost:8888 yourcscusername@kvasi.csc.fi

2. Open browser link: http://127.0.0.1:8890/?token=123456abcdef
```

3. Start an SSH tunnel, forwarding the Jupyter port to a local port number.
You can choose, _e.g_, `8890` for the local port
    * The details of how to open up the SSH tunnel depend on your SSH client.
    * Using the command line, you can login once more from a second terminal,
    now specifying port forwarding, using the ssh command of the output above.

4. Open up your browser, and go to the address given by the output, for example
`http://127.0.0.1:8890/?token=123456abcdef` This should open up the web interface
to Kvasi, with two main options to explore:
    * **The manual** (to the left)
    * **The Jupyter notebook environment** with examples (to the right)


## myQLM

myQLM is a light-weight version of the QLM ecosystem that can be run outside the Kvasi QLM. With myQLM, you can design and simulate quantum algorithms locally, on your own computer. MyQLM is well suited for getting started with quantum algorithm exploration. Advanced features of the QLM are missing, but the basic features are the same.

myQLM is now open access, and can be downloaded for Linux and Windows here:
[myQLM docs and installation instructions](https://myqlm.github.io/index.html)

You can also use myQLM directly from the [CSC Notebooks environment](https://notebooks.csc.fi).
After logging in, simply launch a new "myQLM Notebooks" environment and open it in your browser.
Training material related to previous course can be found under the Folder **CourseMaterial**


## Links

* [Webinar: Quantum Computing and Programming in Two Hours (2021)](https://youtu.be/whoTr3zM3jU)
* [Webinar: Kvanttilaskentaa ja -ohjelmointia kahdessa tunnissa (2021)](https://youtu.be/EnDKcCAjRtg)
* [Webinar: What is Quantum Computing? (2019)](https://www.csc.fi/web/training/-/quantum-computing)
* [Online: Introduction to Quantum Computing and Algorithms](https://ssl.eventilla.com/event/mZ9Pa)
* [The Quantum Learning Machine at atos.net](https://atos.net/en/solutions/quantum-learning-machine)

---
Latest update: 27 Nov 2020
