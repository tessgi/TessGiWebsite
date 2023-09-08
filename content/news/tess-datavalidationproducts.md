Title: Data Validation Products updated for Sector 66
Date: 2023-09-08 13:00
Author: Rebekah Hounsell

We would like to draw to your attention the following issue with the TESS Data Validation (DV) results.

The data validation products (full- and mini-report PDFs, one-page TCE report summary PDFs, time series FITS files, and DV results XML files) for Sector 66 have been updated. The target pixel and light curve FITS files for Sector 66 have not been updated, however. The data validation module was inadvertently run twice in the SPOC pipeline at NASA Ames. The first delivery included intermixed products from the two runs. The data validation algorithms are deterministic, but time limits while running the DV module can affect results for individual target stars. This update provides a fully consistent set of data validation products for Sector 66.

The files in the new delivery replace existing archival products with identical file names. The updated data validation time series products can best be identified by examining the "DATE" keyword, which identifies the date that the file was created. Any time series file with a DATE of "2023-08-25" corresponds to an updated data product. Furthermore, the generation date ("Date Generated") displayed on the stand-alone one-page TCE summaries should exactly match the generation date on the one-page summaries displayed at the beginning of the data validation mini-report for the same target star.

We suggest that any/all Sector 66 data validation product(s) downloaded from MAST prior to 2023-09-06 be replaced with an updated version. After 2023-09-06, the old files will no longer be available.



