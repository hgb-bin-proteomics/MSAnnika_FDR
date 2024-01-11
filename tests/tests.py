#!/usr/bin/env python3

# MS ANNIKA FDR VALIDATOR - TESTS
# 2024 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

# crosslink file without fdr should not do anything
def test1_msannika_fdr():

    from msannika_fdr import main

    result = main(["DSSO_Crosslinks.xlsx"])

    assert len(result) == 0

# crosslink file with fdr should validate
def test2_msannika_fdr():

    from msannika_fdr import main

    result = main(["DSSO_Crosslinks.xlsx", "-fdr", "0.01"])

    # check nr of results
    assert len(result) == 1

    # check nr of crosslinks
    assert result[0].shape[0] == 714

    # check fdr
    assert result[0][result[0]["Decoy"] == True].shape[0] / result[0][result[0]["Decoy"] == False].shape[0] < 0.01

# crosslink file with fdr should validate
def test3_msannika_fdr():

    from msannika_fdr import main

    result = main(["DSSO_Crosslinks.xlsx", "-fdr", "1"])

    # check nr of results
    assert len(result) == 1

    # check nr of crosslinks
    assert result[0].shape[0] == 714

    # check fdr
    assert result[0][result[0]["Decoy"] == True].shape[0] / result[0][result[0]["Decoy"] == False].shape[0] < 0.01

# crosslink file with fdr should validate
def test4_msannika_fdr():

    from msannika_fdr import main

    result = main(["DSSO_Crosslinks.xlsx", "-fdr", "0.05"])

    # check nr of results
    assert len(result) == 1

    # check nr of crosslinks
    assert result[0].shape[0] == 807

    # check fdr
    assert result[0][result[0]["Decoy"] == True].shape[0] / result[0][result[0]["Decoy"] == False].shape[0] < 0.05

# csms file without fdr should group
def test5_msannika_fdr():

    from msannika_fdr import main

    result = main(["DSSO_CSMs.xlsx"])

    # check nr of results
    assert len(result) == 1

    # check nr of grouped crosslinks
    assert result[0].shape[0] == 3192

# csms file with fdr should validate
def test6_msannika_fdr():

    from msannika_fdr import main
    from msannika_fdr import MSAnnika_CSM_Validator as csm_val

    result = main(["DSSO_CSMs.xlsx", "-fdr", "0.01"])

    # check nr of results
    assert len(result) == 3

    #### crosslinks ####

    # check nr of grouped crosslinks
    assert result[0].shape[0] == 3192

    #### validated crosslinks ####

    # check nr of validated crosslinks
    assert result[2].shape[0] == 714

    # check fdr of validated crosslinks
    assert result[2][result[2]["Decoy"] == True].shape[0] / result[2][result[2]["Decoy"] == False].shape[0] < 0.01

    #### validated csms ####

    # check nr of validated csms
    assert result[1].shape[0] == 3021

    # check fdr of validated csms
    result[1]["Class"] = result[1].apply(lambda row: csm_val.get_class(row), axis = 1)
    assert result[1][result[1]["Class"] == "Decoy"].shape[0] / result[1][result[1]["Class"] == "Target"].shape[0] < 0.01

# csms file with fdr should validate
def test7_msannika_fdr():

    from msannika_fdr import main
    from msannika_fdr import MSAnnika_CSM_Validator as csm_val

    result = main(["DSSO_CSMs.xlsx", "-fdr", "1"])

    # check nr of results
    assert len(result) == 3

    #### crosslinks ####

    # check nr of grouped crosslinks
    assert result[0].shape[0] == 3192

    #### validated crosslinks ####

    # check nr of validated crosslinks
    assert result[2].shape[0] == 714

    # check fdr of validated crosslinks
    assert result[2][result[2]["Decoy"] == True].shape[0] / result[2][result[2]["Decoy"] == False].shape[0] < 0.01

    #### validated csms ####

    # check nr of validated csms
    assert result[1].shape[0] == 3021

    # check fdr of validated csms
    result[1]["Class"] = result[1].apply(lambda row: csm_val.get_class(row), axis = 1)
    assert result[1][result[1]["Class"] == "Decoy"].shape[0] / result[1][result[1]["Class"] == "Target"].shape[0] < 0.01

# csms file with fdr should validate
def test8_msannika_fdr():

    from msannika_fdr import main
    from msannika_fdr import MSAnnika_CSM_Validator as csm_val

    result = main(["DSSO_CSMs.xlsx", "-fdr", "0.05"])

    # check nr of results
    assert len(result) == 3

    #### crosslinks ####

    # check nr of grouped crosslinks
    assert result[0].shape[0] == 3192

    #### validated crosslinks ####

    # check nr of validated crosslinks
    assert result[2].shape[0] == 807

    # check fdr of validated crosslinks
    assert result[2][result[2]["Decoy"] == True].shape[0] / result[2][result[2]["Decoy"] == False].shape[0] < 0.01

    #### validated csms ####

    # check nr of validated csms
    assert result[1].shape[0] == 3331

    # check fdr of validated csms
    result[1]["Class"] = result[1].apply(lambda row: csm_val.get_class(row), axis = 1)
    assert result[1][result[1]["Class"] == "Decoy"].shape[0] / result[1][result[1]["Class"] == "Target"].shape[0] < 0.01
