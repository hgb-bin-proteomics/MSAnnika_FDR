#!/usr/bin/env python3

# MS ANNIKA FDR VALIDATOR - TESTS
# 2024 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

# test 1
def test1_msannika_fdr():

    from msannika_fdr import main

    result = main(["DSSO_CSMs.xlsx"])

    assert True
