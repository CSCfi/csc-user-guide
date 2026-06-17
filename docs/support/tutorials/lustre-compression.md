# Advanced: Changing the Lustre compression settings for a file or directory in Roihu

!!! warning "Proceed with caution"
     Changing Lustre compression settings should only be done for data that you can afford to lose.
     When enabling compression, there is always a small risk of data corruption.
     Change these settings only when you can verify that your data is intact,
     and keep a separate copy of important data in another location.

This tutorial shows how to inspect and change the compression settings for files and directories on Roihu.

For background on Lustre concepts such as OSTs, MDTs, metadata operations and file striping, see documentation on the [Lustre file system](../../computing/lustre.md). For broader I/O performance tuning, see the [Lustre performance optimization tutorial](./lustre_performance.md).

Changing the compression scheme on Lustre, or disabling it, can impact how much disk space your files use on the system, and can impact I/O performance of those files.

Most users should use the default (uncompressed) Lustre settings. On Roihu, the defaults are suitable for general use and should not be changed unless there is a clear reason to test a different compression setting.

For some workloads, where data can compress well, or where the data is
written infrequently or sequentially, but read often, compression can provide
a significant performance increase for I/O operations.

## Roihu default file layout

On Roihu, new files use the following default Lustre layout:

| Setting | Default |
|---------|---------|
| Stripe count | 1 |
| Stripe size | 4 MiB |
| Compression | disabled |
| Compression algorithm | none |
| Compression level | N/A |
| Compression chunk size | N/A |

## Check the current layout

Use `lfs getstripe` to inspect the layout of a file or directory:

```bash
lfs getstripe <file-or-directory>
```

For a file, this shows the layout used by that file.
For a directory, it shows the layout inherited by new files created in that directory.

Example:

```bash
lfs getstripe my_file
```

Giving you the output:

```text
my_file
  lcm_layout_gen:    1
  lcm_mirror_count:  1
  lcm_entry_count:   1
    lcme_id:             1
    lcme_mirror_id:      0
    lcme_flags:          init,compress
    lcme_extent.e_start: 0
    lcme_extent.e_end:   EOF
    lcme_compr_type:     none
    lcme_compr_lvl:      0
    lcme_compr_chunk_kb: 64
      lmm_stripe_count:  1
      lmm_stripe_size:   4194304
      lmm_pattern:       raid0,compress
      lmm_layout_gen:    0
      lmm_stripe_offset: 0
      lmm_objects:
      - 0: { l_ost_idx: 0, l_fid: [0x300001b70:0x1b5a645:0x0] }
```

in a file created with the default settings, with compression disabled.

## Modifying the Lustre compression configuration

Roihu does not enable Lustre compression for new files, by default.
However, Lustre compression can reduce physical storage usage for compressible data,
and may reduce the amount of data transferred between the storage system and compute nodes.

The effect on performance depends on the application, file format and I/O pattern.
Data that is already compressed, encrypted or otherwise difficult to compress may benefit less.

Compression may also add overhead, especially for write-heavy workloads.

### Changing the compression algorithm

Changing the compression inherited by new files is done with the `lfs setstripe` command, that also affects file striping.
For choosing the best stripe settings for your workload, see the
[general Lustre striping instructions](../../computing/lustre.md#file-striping-and-alignment).

You can turn compression on in the following fashion
for a folder or a new file:

```bash
lfs setstripe \
  --stripe-size 4M \
  --stripe-count 1 \
  --compress zstd:3 \
  --compress-chunk 1M \
  new_layout_dir
```

In the above example, we use the Roihu default stripe settings, but
apply also a compression algorithm (`zstd`), with a compression level 3. Compression chunk is set to 1M.

For choosing between different algorithms, see `man lfs setstripe` on Roihu.
In CSC testing, performance differences between the different algorithms
have typically been small. The default `zstd` level 3 provides the best compression ratios
with good performance for general use, and is the option we recommend to start with.

### Changing the compression chunk size

The compression chunk size controls how much data is compressed as one unit.
A good starting value we recommend is 1 MiB.

In general, larger chunks may improve the compression ratio, while smaller chunks may be better for workloads that perform many small or random reads and writes.
However, the best value depends on the application, file format and I/O pattern.

Changing the compression chunk size is an advanced tuning option and is not recommended unless you have a specific reason to test it.
The default value should be used for most workloads.

## Change the layout of existing data

A Lustre file layout is fixed when the file is created, and the stripe and compression configuration is **persistent**.
Moving a file within the same Lustre file system does not change its layout.

To change the layout of existing data, create a new file or directory with the desired layout and copy the data there.

For example:

```bash
mkdir new_layout_dir

lfs setstripe \
  --stripe-size 4M \
  --stripe-count 1 \
  --compress zstd:3 \
  --compress-chunk 1M \
  new_layout_dir

cp old_file new_layout_dir/
```

Do not use `mv` if your goal is to change the file layout.