# Kvasi

## The Quantum Learning Machine

Quantum computers differ from their classical counterparts when it comes to the basic computational operators. Before QPUs can be utilized, they require tailor-made programs and algorithms. With Kvasi, the user can explore and develop algorithms for quantum computers.

Kvasi provides an ecosystem for developing and simulating quantum algorithms in both ideal, and realistic, noisy conditions. With Kvasi, you can optimize your algorithm for a specific hardware (QPU), with specific connections and basic gate operations.

The algorithms can be developed either at a level close to the hardware, using the Atos Quantum Assembler (AQASM) language, or using a higher level, Python based language and ready-made libraries. The QLM comes with several ready-made examples.

## Accessing Kvasi

Kvasi is accessed through Puhti (puhti.csc.fi). Thus, you first need a CSC userid for Puhti. If you do not have one, check out the [How to get started as a new user at CSC?](../support/faq/how-to-get-started-at-CSC.md) FAQ.

In order to access Kvasi, your CSC userid needs to part of the `kvasi-users` group. Send a mail to servicedesk@csc.fi and ask to be added to the **kvasi-users** group.

When you have been added, you can use SSH to login to kvasi.csc.fi from/via Puhti.

#### Setting up an SSH tunnel for the Jupyter web interface

In order to use the Jupyter notebook environment, you need to set up an SSH tunnel, forwarding the output port of your notebook environment to your local computer. You need to go through Puhti, that is, use Puhti as a "jump host". Follow these steps:

1. Login to Kvasi with SSH:
  - From Puhti: `ssh <userid>@kvasi.csc.fi`
  - From another machine: `ssh -J <userid>@puhti.csc.fi <userid>@kvasi.csc.fi`
  - If your ssh command does not understand the "-J" flag, use an an alternative syntax:
    - `ssh -o ProxyCommand="ssh -W %h:%p <userid>@puhti.csc.fi" <userid>@kvasi.csc.fi`
2. Start the Jupyter server: `./qlm_notebook/launch_qlm_notebook`. This will give you two values:
  - The Jupyter port number. It will be `8888`, or higher
  - The token for accessing the web interface (a string of letters and numbers)
  - Example output:

```
Jupyter port : 8888
Jupyter token: 123456abcdef

To access your Jupyter notebook from your local computer:

1. Create SSH tunnel:
    (a) ssh -L 8890:localhost:8888 -J <userid>@puhti.csc.fi <userid>@kvasi.csc.fi
 or (b) ssh -L 8890:localhost:8888 -o ProxyCommand="ssh -W %h:%p <userid>@puhti.csc.fi" <userid>@kvasi.csc.fi

2. Open browser link: http://127.0.0.1:8890/?token=123456abcdef
```

4. Start an SSH tunnel, forwarding the Jupyter port to a local port number. You can choose, _e.g_, `8890` for the local port
  - The details of how to open up the SSH tunnel depend on your SSH client.
  - Using the command line, you can login once more from a second terminal, now specifying port forwarding, using the ssh command of the output above.

5. Open up your browser, and go to the address given by the output, for example `http://127.0.0.1:8890/?token=123456abcdef` This should open up the web interface to Kvasi, with two main options to explore:
  - **The manual** (to the left)
  - **The Jupyter notebook environment** with examples (to the right)


## myQLM

MyQLM is a light-weight version of the QLM ecosystem that can be run outside the Kvasi QLM. With myQLM, you can design and simulate quantum algorithms locally, on your own computer. MyQLM is well suited for getting started with quantum algorithm exploration. Advanced features of the QLM are missing, but the basic features are the same.

To get access to myQLM, contact the CSC service desk, servicedesk@csc.fi. Use the hashtag #kvasi to facilitate sorting.

## Links
[Webinar: What is Quantum Computing?](https://www.csc.fi/web/training/-/quantum-computing)

[The Quantum Learning Machine at atos.net](https://atos.net/en/solutions/quantum-learning-machine)

---
Latest update: 25 May 2020
