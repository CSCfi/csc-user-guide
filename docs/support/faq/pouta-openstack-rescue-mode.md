# Server can't boot. How to rescue instances?

In case you run into a situation where your kernel upgrade fails for some reason, and your CentOS 7 instance won't come up, you might find these instructions useful. Sometimes this might seem like a failed resize but the real reason is the restart that a resize requires.

## Symptoms

Check your instance Console Log (web UI: Instances -> <your instance> -> Log)

	[    1.041853] Loading compiled-in X.509 certificates
	[    1.043433] Loaded X.509 cert 'CentOS Linux kpatch signing key:ea0413152cde1d98ebdca3fe6f0230904c9ef717'
	[    1.046556] Loaded X.509 cert 'CentOS Linux Driver update signing key:7f421ee0ab69461574bb358861dbe77762a4201b'
	[    1.050310] Loaded X.509 cert 'CentOS Linux kernel signing key:d4115f110055db56c8d605ab752173cfb1ac54d8'
	[    1.053448] registered taskstats version 1
	[    1.055861] Key type trusted registered
	[    1.057771] Key type encrypted registered
	[    1.059249] IMA: No TPM chip found, activating TPM-bypass! (rc=-19)
	[    1.061680]   Magic number: 14:548:18
	[    1.063246]  ep_81: hash matches
	[    1.064844] rtc_cmos 00:00: setting system clock to 2018-08-23 08:02:54 UTC(1535011374)
	[    1.067954] md: Waiting for all devices to be available before autodetect
	[    1.069982] md: If you don't use raid, use raid=noautodetect
	[    1.072041] md: Autodetecting RAID arrays.
	[    1.073689] md: autorun ...
	[    1.074976] md: ... autorun DONE.
	[    1.076358] List of all partitions:
	[    1.077771] No filesystem could mount root, tried: 
	[    1.079600] Kernel panic - not syncing: VFS: Unable to mount root fs onunknown-block(0,0)
	[    1.082286] CPU: 1 PID: 1 Comm: swapper/0 Not tainted 3.10.0-862.11.6.el7.x86_64 #1
	[    1.085033] Hardware name: Fedora Project OpenStack Nova, BIOS 0.5.1 01/01/2011
	[    1.087639] Call Trace:
	[    1.088800]  [<ffffffff871135d4>] dump_stack+0x19/0x1b
	[    1.090453]  [<ffffffff8710d11f>] panic+0xe8/0x21f
	[    1.091982]  [<ffffffff8776c761>] mount_block_root+0x291/0x2a0
	[    1.093704]  [<ffffffff8776c7c3>] mount_root+0x53/0x56
	[    1.095394]  [<ffffffff8776c902>] prepare_namespace+0x13c/0x174
	[    1.097281]  [<ffffffff8776c3df>] kernel_init_freeable+0x1f8/0x21f
	[    1.099244]  [<ffffffff8776bb1f>] ? initcall_blacklist+0xb0/0xb0
	[    1.101131]  [<ffffffff87101bc0>] ? rest_init+0x80/0x80
	[    1.102813]  [<ffffffff87101bce>] kernel_init+0xe/0xf0
	[    1.104497]  [<ffffffff871255f7>] ret_from_fork_nospec_begin+0x21/0x21
	[    1.106367]  [<ffffffff87101bc0>] ? rest_init+0x80/0x80
	[    1.107997] Kernel Offset: 0x5a00000 from 0xffffffff81000000 (relocation range:0xffffffff80000000-0xffffffffbfffffff)


The log says that the instance couldn't boot because it can't find root "Kernel panic - not syncing: VFS: Unable to mount root fs onunknown-block(0,0)". The fix is to use (some) previous, working kernel. Since you can't boot the server, you have to make the fix to the Volume (boot files) by using another instance.

## How to fix the issue

Note, that you will modify grub, there are probably better ways to do it, so do not be afraid to see what other guides there are on the internet. This FAQ is mostly meant to show that there is a command named `nova rescue`. There is also a command named `openstack server rescue` which is almost the same as `nova rescue` but is missing the `--image` flag which is almost *always* required when rescuing servers.

1. shutdown the instance <pre><code>openstack server stop $INSTANCE_UUID</pre></code>
2. Use this command to rescue the instances. <pre><code>nova rescue $INSTANCE_UUID --image CentOS-7</pre></code>
1. Make sure that the instance is in rescue mode with <pre><code>openstack server show $INSTANCE_UUID</pre></code>
3. ssh into the instances.
3. Check what volumes you have. If you don't have any other volumes attached it should looks something like this:
<pre><code>$ lsblk
NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
vda    253:0    0  10G  0 disk
└─vda1 253:1    0  10G  0 part
vdb    253:16   0  80G  0 disk
└─vdb1 253:17   0  80G  0 part /
</code></pre>
4. Now you want to mount `vdb1` to /tmp/mnt and go to that directory. <pre><code>$ sudo mkdir -p /tmp/mnt; sudo mount /dev/vdb1 /tmp/mnt/</code></pre>
5. Take a backup of grub <pre><code>$ cp /tmp/mnt/boot/grub2/grub.cfg /tmp/mnt/root/grub.cfg.bak-`date +"%F"`</pre></code>
7. Open `/tmp/mnt/boot/grub2/grub.cfg` with your favorite text editor. Remove the first `menuentry` section. *NOTE:* This might not be the correct solution for your specific problem
8. Log out from the instances and `unrescue` the instance <pre><code>nova unrescue $INSTANCE_UUID</pre></code>
9. If the instance comes up successfully ssh into the instance and reinstall the kernel
    <pre><code>yum reinstall kernel</pre></code>
10. It would be a good idea to verify that a restart works after the kernel reinstallation. 

