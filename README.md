![workflow_state](https://github.com/hgb-bin-proteomics/MSAnnika_FDR/workflows/msannika_fdr/badge.svg)

# MS Annika FDR

A script and functions to group and validate [MS Annika](https://github.com/hgb-bin-proteomics/MSAnnika)
results. The main use case would be for re-validating results after filtering or
merging results from different MS Annika runs.

## Usage

- Install python 3.7+: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Install requirements: `pip install -r requirements.txt`
- Export MS Annika results from Proteome Discoverer to Microsoft Excel format.
- Run `python msannika_fdr.py filename.xlsx -fdr 0.01` (see below for more examples).
- The script may take a few minutes, depending on the number of CSMs/crosslinks to process.
- Done!

## Examples

`msannika_fdr.py` takes one positional and one flagged argument. The first
argument always has to be the filename(s) of the MS Annika result file(s). You
may specify any number of result files, keep in mind however that
`msannika_fdr.py` will process these files seperately, if you want to merge
several result files, check out [MS Annika Combine Results](https://github.com/hgb-bin-proteomics/MSAnnika_Combine_Results).
For demonstration purposes we will use the files supplied in the `/data` folder.
`DSSO_Crosslinks.xlsx` contains unvalidated crosslinks from an MS Annika search,
`DSSO_CSMs.xlsx` contains unvalidated CSMs from an MS Annika search.

The following is a valid `msannika_fdr.py` call:

```bash
python msannika_fdr.py DSSO_Crosslinks.xlsx
```

This will not do anything because no FDR was given. You should see in the output
that the script skipped the file. However, doing the same with a CSM file
results in a different output:

```bash
python msannika_fdr.py DSSO_CSMs.xlsx
```

This will group the CSMs by sequence and position to crosslinks and you should
see a file `DSSO_CSMs_crosslinks.xlsx` generated.

If you suppy the argument `-fdr` or `--false_discovery_rate` and the desired FDR
as a floating point number, the results will be validated:

```bash
python msannika_fdr.py DSSO_Crosslinks.xlsx -fdr 0.01
```

This will validate the input crosslinks for estimated 1% FDR and will generate a
a file called `DSSO_Crosslinks_validated.xlsx` containing only crosslinks above
the estimated 1% FDR threshold. Note that the following command will produce the
same output:

```bash
python msannika_fdr.py DSSO_Crosslinks.xlsx -fdr 1
```

Validating a CSMs file works the same way:

```bash
python msannika_fdr.py DSSO_CSMs.xlsx -fdr 0.01
```

This will will validate the input CSMs for estimated 1% FDR and will generate a
a file `DSSO_CSMs_validated.xlsx` containing only CSMs above the estimated 1%
FDR threshold. Furthermore, it will group the input CSMs to crosslinks and
output them to the file `DSSO_CSMs_crosslinks.xlsx` and the validate those
crosslinks for 1% estimated FDR and store the result in
`DSSO_CSMs_crosslinks_validated.xlsx`

You can also supply several files to the script like this:

```bash
python msannika_fdr.py DSSO_CSMs.xlsx DSSO_Crosslinks.xlsx -fdr 0.01
```

This will process the input files seperately and sequentially and produce the
as mentioned above:
- `DSSO_Crosslinks_validated.xlsx`
- `DSSO_CSMs_validated.xlsx`
- `DSSO_CSMs_crosslinks.xlsx`
- `DSSO_CSMs_crosslinks_validated.xlsx`

## Parameters

```python
"""
DESCRIPTION:
A script to group and validate results from MS Annika searches.
USAGE:
msannika_fdr.py f [f ...]
                  [-fdr FDR][--false_discovery_rate FDR]
                  [-h][--help]
                  [--version]
positional arguments:
  f                     MS Annika result files in Microsoft Excel format (.xlsx)
                        to process.
optional arguments:
  -fdr FDR, --false_discovery_rate FDR
                        False discovery rate to validate results for. Supports
                        both percentage input (e.g. 1) or fraction input (e.g.
                        0.01). By default not set and the input results will
                        just be grouped to crosslinks (if CSMs as input) or
                        nothing will be done (if crosslinks as input).
                        Default: None
  -h, --help            show this help message and exit
  --version             show program's version number and exit
"""
```

## Known Issues

[List of known issues](https://github.com/hgb-bin-proteomics/MSAnnika_FDR/issues)

## Citing

If you are using the MS Annika FDR script please cite:
```
MS Annika 2.0 Identifies Cross-Linked Peptides in MS2–MS3-Based Workflows at High Sensitivity and Specificity
Micha J. Birklbauer, Manuel Matzinger, Fränze Müller, Karl Mechtler, and Viktoria Dorfer
Journal of Proteome Research 2023 22 (9), 3009-3021
DOI: 10.1021/acs.jproteome.3c00325
```

If you are using MS Annika please cite:
```
MS Annika 2.0 Identifies Cross-Linked Peptides in MS2–MS3-Based Workflows at High Sensitivity and Specificity
Micha J. Birklbauer, Manuel Matzinger, Fränze Müller, Karl Mechtler, and Viktoria Dorfer
Journal of Proteome Research 2023 22 (9), 3009-3021
DOI: 10.1021/acs.jproteome.3c00325
```
or
```
MS Annika: A New Cross-Linking Search Engine
Georg J. Pirklbauer, Christian E. Stieger, Manuel Matzinger, Stephan Winkler, Karl Mechtler, and Viktoria Dorfer
Journal of Proteome Research 2021 20 (5), 2560-2569
DOI: 10.1021/acs.jproteome.0c01000
```

## License

- [MIT](https://github.com/hgb-bin-proteomics/MSAnnika_FDR/blob/master/LICENSE)

## Contact

- [micha.birklbauer@fh-hagenberg.at](mailto:micha.birklbauer@fh-hagenberg.at)
