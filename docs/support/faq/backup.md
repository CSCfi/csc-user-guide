---
search:
  boost: 100
---

# Does CSC back up my data on Roihu?

**No**. None of Roihu's disk areas (`$HOME`, `/projappl`, `/scratch` and
`/dataset`) are automatically backed up by CSC. **Data that is accidentally
deleted by the user or otherwise lost, cannot be recovered**. The same applies
for [disk areas on LUMI](https://docs.lumi-supercomputer.eu/storage/).

It is the user's own responsibility to keep backup copies of any data they
want to preserve, for example in [Allas](../../data/Allas/index.md) or
[LUMI-O](https://docs.lumi-supercomputer.eu/storage/lumio/). The
[allas-backup tool](../../data/Allas/using_allas/a_backup.md) provides an easy
way to make such backups.

In addition to not being backed up, note that Roihu's `/scratch` disk area is
also periodically cleaned of files that have not been accessed in a while. See
the [Usage policy](../../computing/usage-policy.md#disk-cleaning) page for
details.

## More information

* [Roihu disk areas](../../computing/roihu-disk.md)
* [Where should I put my data?](where-should-i-put-my-data.md)
* [Managing data on supercomputer scratch disks](../tutorials/clean-up-data.md)
