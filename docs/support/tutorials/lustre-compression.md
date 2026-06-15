# Advanced: Changing the Lustre striping and compression settings for a file or directory in Roihu

This tutorial shows how to inspect and change Lustre file striping and compression settings for files and directories on Roihu.

For background on Lustre concepts such as OSTs, MDTs, metadata operations and file striping, see [Lustre file system](../../computing/lustre.md).
For broader I/O performance tuning, see the [Lustre performance optimization tutorial](lustre_performance.md).

Changing the file striping settings in Lustre can allow the workload to take advantage of parallel I/O and multiple OSTs.

Changing the compression scheme on Lustre, or disabling it, can impact
how much disk space your files use on the system, and can impact I/O performance
of those files.

Most users should use the default Lustre settings. On Roihu, the defaults are suitable for general use
and should not be changed unless there is a clear reason to test a different layout.

!!! warning "Use custom Lustre settings only for well-understood I/O workflows"
    Changing Lustre striping or compression is an advanced operation.
    Use custom settings only if you understand your software's I/O behavior and the characteristics of the files it reads or writes.

    In practice, this usually means that you know whether the application performs serial or parallel I/O,
    whether it works with large shared files or many small files,
    how many processes perform I/O, and whether I/O has been identified as a performance bottleneck.
    Profiling or benchmarking with the real application and realistic data
    is strongly recommended before changing any Lustre layout settings.

    Incorrect striping or compression settings can reduce performance and increase load on the shared file system.

## Roihu default file layout

On Roihu, new files use the following default Lustre layout:

| Setting | Default |
|---------|---------|
| Stripe count | 1 |
| Stripe size | 4 MiB |
| Compression | enabled |
| Compression method | Zstandard |
| Compression level | 3 |
| Compression chunk size | 1 MiB |

A stripe count of 1 means that files are not striped across multiple OSTs by default.

When manually changing striping on Roihu, include the compression options if you want to keep the default compression behavior:

```bash
--compress zstd:3 --compress-chunk 1M
```

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
    lcme_compr_type:     zstd
    lcme_compr_lvl:      3
    lcme_compr_chunk_kb: 1024
      lmm_stripe_count:  1
      lmm_stripe_size:   4194304
      lmm_pattern:       raid0,compress
      lmm_layout_gen:    0
      lmm_stripe_offset: 1
      lmm_objects:
      - 0: { l_ost_idx: 1, l_fid: [0x340003abc:0x17ff66d:0x0] }
```

in a file created with the default settings.

## Set layout for new files in a directory

To set a custom layout for new files created in a directory, use `lfs setstripe` on the directory.

For example, to set a stripe count of 4 and stripe size of 4 MiB while keeping the default Roihu compression settings:

```bash
mkdir large_output_dir

lfs setstripe \
  --stripe-size 4M \
  --stripe-count 4 \
  --compress zstd:3 \
  --compress-chunk 1M \
  large_output_dir
```

Files created after this in `large_output_dir` inherit the directory layout.

Check the directory layout with:

```bash
lfs getstripe large_output_dir
```

!!! note
    Setting the layout for a directory affects new files created in that directory. It does not change the layout of files that already exist.

## Create a new file with a custom layout

You can also create a new empty file with a custom layout:

```bash
lfs setstripe \
  --stripe-size 4M \
  --stripe-count 4 \
  --compress zstd:3 \
  --compress-chunk 1M \
  new_file
```

After creating the file, write data to it with your application or copy data into it.

## Change the layout of existing data

A Lustre file layout is fixed when the file is created. And the stripe and compression configuration is persistent.
Moving a file within the same Lustre file system does not change its layout.

To change the layout of existing data, create a new file or directory with the desired layout and copy the data there.

For example:

```bash
mkdir new_layout_dir

lfs setstripe \
  --stripe-size 4M \
  --stripe-count 4 \
  --compress zstd:3 \
  --compress-chunk 1M \
  new_layout_dir

cp old_file new_layout_dir/
```

Do not use `mv` if your goal is to change the file layout.

## Choosing a stripe count

There is no single stripe count that is best for all applications.
The best value depends on the file size, I/O pattern and the number of processes doing parallel I/O.

General guidance:

* Use the default stripe count of 1 for small files.
* Consider a larger stripe count only for large files accessed in parallel.
* Do not use more stripes than the number of processes that perform I/O.
* Avoid unnecessarily large stripe counts, as they can increase overhead and contention.
* Test with your real application and realistic data before using a custom layout in production.
* Increase striping count for parallel access, especially on large files:
    * The striping factor should be a factor of the number of used processes performing parallel I/O
    * A rule of thumb is to use as striping the square root of the file size in GB. If the file is 90 GB, the square root is 9.5, so use at least 9 OSTs.
    * If you use, for example, 16 MPI processes for parallel I/O, the number of the used OSTs should be less or equal to 16.

For broader I/O tuning guidance, see [Lustre performance optimization tutorial](lustre_performance.md).

## Modifying the Lustre compression configuration

Roihu enables Lustre compression by default for new files.
Compression can reduce physical storage usage for compressible data, and may reduce the amount of data transferred between the storage system and compute nodes.

The effect on performance depends on the application, file format and I/O pattern. Data that is already compressed, encrypted or otherwise difficult to compress may benefit less.

Compression may also add overhead, especially for write-heavy workloads.

### Disabling compression

You can choose to disable compression for all new files created under a folder:

```bash
lfs setstripe \
  --stripe-size 4M \
  --stripe-count 1 \
  --compress none \
  uncompressed_dir
```

The stripe size and stripe count can be chose independently from the compression options.

### Changing the compression algorithm

Alternatively, you can choose a different compression algorithm (e.g. `lz4`)
for a folder or a new file:

```bash
lfs setstripe \
  --stripe-size 4M \
  --stripe-count 4 \
  --compress lz4:1 \
  --compress-chunk 1M \
  new_layout_dir
```

For choosing between different algorithms, see `man lfs setstripe` on Roihu.
In CSC testing, performance differences between the different algorithms
have typically been small. The default `zstd` level 3 provides the best compression ratios
with good performance for general use.

### Changing the compression chunk size

The compression chunk size controls how much data is compressed as one unit.
On Roihu, the default compression chunk size is 1 MiB.

In general, larger chunks may improve the compression ratio, while smaller chunks may be better for workloads that perform many small or random reads and writes.
However, the best value depends on the application, file format and I/O pattern.

Changing the compression chunk size is an advanced tuning option and is not recommended unless you have a specific reason to test it.
The default value should be used for most workloads.

For example, to set the compression chunk size to 512 KiB for new files created in a directory:

```bash
lfs setstripe \
  --stripe-size 4M \
  --stripe-count 1 \
  --compress zstd:3 \
  --compress-chunk 512K \
  custom_chunk_dir
```

Verify the layout with:

```bash
lfs getstripe custom_chunk_dir
```