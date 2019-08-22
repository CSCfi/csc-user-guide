# How do I copy my files from Taito/Sisu to Puhti

The new computing environment has a separate storage system from the old computing environment of Taito and Sisu. Therefore, data must be copied over from the old storage to the new one. As we here at CSC are not really aware of what data you have on our disks it is best if you – as an expert of it – take care of copying your data over. After all, you know best which data you will need in the new environment.

When deciding what data to copy over remember that there are at least three locations to look into: your home directory `$HOME`, your applications directory `$USERAPPL`, and your work directory `$WRKDIR`. If you are part of a project group, please check also your project directories – and if you are the PI then this is even more important!

We understand that copying might not be as easy as it sounds but here's some help for that. And there's always someone at our [helpdesk](mailto:servicedesk@csc.fi) to answer your all questions and guide you forward.

## Copy files with scp

The most simple way to copy your files from Taito/Sisu is to use scp, Secure Copy. Assuming you have already set up public key authentication for ssh, copying is as straightforward as:

```
scp -T -c blowfish-cbc -o Compression=no -x -p -r ./* puhti:
```

This command will copy all files from current directory (`./*`) with all directories underneath it (`-r`) preserving their timestamps (`-p`) to puhti (`puhti:`). In addition, we are telling ssh to do some tweaks to gain more speed by using the fastest – and weakest – reasonable encryption algorithm (`-c blowfish-cbc`) without compression (`-o Compression=no`), a pseudo-tty (`-T`), and X11 forwarding.

And if you haven't set up public key authentication, don't worry. It is still exactly the same command, but there's one extra step: you need to type in your Puhti account's password when prompted.

However, this approach might not be the most convenient one if you have a multitude of files or they a huge in size. Or both.

## Copy files using rsync

Another possibility is to use rsync tool. As the name suggests, it is a tool to syncronise files between two storages and it can gain substantial time savings compared to scp as it only copies modified bits in files. But as we are making a fresh copy of your files from one location to another there's really no way around the fact that every single bit must be copied over.

```
rsync -e "ssh -T -c blowfish-cbc -o Compression=no -x" -u -P -a ./* puhti:
```

With this command we copy all files from current directory (`./*`) and all directories underneath it preserving all file attributes (`-a`) to puhti (`puhti:`). The update option `-u` is there for emergencies: in case copying is interrupted for one reason or another rsync will not copy again those files already successfully copied but continues from where it was left (`-P`). We also tell rsync to use the same ssh optimisations that were explained earlier (`-e "ssh …"`).

## Do not copy files with tar and netcat

Using tar and netcat is a bit more efficient way of copying files than scp or rsync as it does not encrypt and decrypt the files in transit. Avoiding this cpu heavy operation means we can feed bits more rapidly to the network and — given that the network has free capacity — the limiting factor is the disk I/O speed.

But this increase in speed doesn't come free. It is a much more _error prone_ method, there's _no error detection_ or correction, and it has _no security_ in it, whatsoever. On top of that, it needs active monitoring and manual checking whether all files were copied correctly.

In general, we do not recommend using this method but for substantially large files (GBs rather than MBs) it is worth considering. However, *we do not provide support* for it.

### But if you still insist…

First, create a list of files you want to copy. For example, this command will create a file `large_files` listing all the files (`-type f`) underneath current directory (`.`) that are bigger than 1 GB (`-size +1G`):

```
find . -type f -size +1G -print > large_files
```

On the receiving end, i.e. Puhti:

```
netcat -l -p 42424 | tar xpf -
```

*NOTE*: instead of 42424 select a random number between 32767 and 65535! If there are two persons using the same number they will mess up each others' data for sure.

Then, on the sending end, e.g. Taito:

```
tar cf - -T large_files | netcat -p 42424 puhti
```

The first command will start `netcat` program, which will listen to any incoming connections (`-l`) on port 42424 (`-p 42424`). Any data that is received from the network to that port will be fed through a pipe (`|`) to `tar` program, which will extract (`x`) files from the tar archive (`f`) read from the pipe and writes them to the disk preserving timestamps (`p`).

The second command will create (`c`) a tar archive (`f`) containing all the files listed in file large_files (`-T large_files`) and writes it through a pipe (`-` and `|`) to `netcat` program, which sends it to `puhti` on port 42424 (`-p 42424`).

Both commands will terminate after the transfer is complete – either by success or any kind of error. There is absolutely no indication of the result and it is up to you to verify that the transfer was actually successful. Calculating MD5 sums might be a good idea (but slows you down…).