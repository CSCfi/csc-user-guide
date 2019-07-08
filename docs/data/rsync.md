## Using rsync for data transfer and synchronization 

**Rsync** is a data transport tool that can be used much like the scp command.
When transferring data, `rsync` checks the difference between the source and target files and only transfers the parts that have changed. This makes `rsync` suitable for:

- Synchronizing folders. Using `scp` or `cp` would copy and transfer everything, while `rsync` will only copy and transfer the modifications. 
- Transferring larger files. `rsync` can be set to save progress, so if the transfer is interrupted it can be resumed at the same point. 



The Basic command syntax of rsync is:

```
rsync -options source target
```

If the data source or target location is a remote site, it is defined with syntax:
```
userame@server:/path/in/server
```
However, both the target and source can also be located on the same machine. In that case you can just give directory paths to source and target sites.

The table below lists the most commonly used  options:

|Option 	| Argument | Description |
|---------------|----------|-------------|
|`-r`		|	   |recurse into directories |
|`-a`		|	   | Use archive mode: copy files and directories recursively and preserve access permissions and time stamps.	 	 |
|`-v`		|	   | 	Verbose mode.	 	 |
|`-z`		|	   |	 Compress	 |
|`-e`		|ssh	   |	 Specify the remote shell to use.	 |
|`-n`		|	   |	Show what files would be transferred. 	 |
|`--partial`	|	   |	Keep partially transferred files. 	 |
|`--progress`	|	   |	Show progress during transfer. 	 |
|`-P`		|	   |	same as --partial --progress 	 |

So the command for transferring a local folder to Taito,while showing the progress and keeping partially transfered files, would be:

```bash
rsync -rP /path/to/local/folder  username@taito.csc.fi:/path/to/target
```
This would either:

- create a folder on Taito at _path/to/target/folder_, if the folder was not present before. In this case, everything in the folder will be transfered
- synchronize the source and target folders, if the folder already exists on Taito. In this case, only changes we have made will be transfered

And the same thing in reverse:

```bash
rsync -rP username@taito.csc.fi:/path/to/target/folder /path/to/local
```

!!! note
	`rsync` will always overwrite any changes made to the target, even if they are newer than the source.

