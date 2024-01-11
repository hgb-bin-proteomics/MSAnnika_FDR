#!/usr/bin/env python3

# MS ANNIKA FDR VALIDATOR - TESTS
# 2024 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

# crosslink file without fdr should not do anything
def test1_msannika_fdr():

    from msannika_fdr import main

    result = main(["DSSO_CSMs.xlsx"])

    assert len(result) == 0

# crosslink file with fdr should validate
def test2_msannika_fdr():

    from msannika_fdr import main

    result = main(["DSSO_CSMs.xlsx", "-fdr", "0.01"])

    # check nr of results
    assert len(result) == 1

    # check nr of crosslinks
    assert result[0].shape[0] == 714

    # check fdr
    assert result[0][result[0]["Decoy"] == False].shape[0] / result[0][result[0]["Decoy"] == True].shape[0] < 0.01
