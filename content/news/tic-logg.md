Title: Error in a small number of TIC v5 surface gravities
Date: 2017-08-01 14:00
Author: Tom Barclay

The surface gravities reported in column 67 of the TESS Input Catalog version 5 (TIC-5), do not accurately represent the expected surface gravities using the reported values for mass (column 73) and radii (column 71). This only affects stars where the stellar properties were calculated using available parallax information (the stellar properties flag is set to "plx" in column 64 and no other quantities in the TIC are affected. TIC users can either calculate the surface gravity using the provided mass and radius values, or use a [provided data file](http://archive.stsci.edu/missions/tess/catalogs/tic_v5/tic5_logg_fix.csv) to access the appropriately calculated values. This fix will be built in to the next version of the TIC, version 6.

Additionally, for TIC v5, numerical columns with values of exactly 0 are actually null values. Starting in TIC v6, these will be properly set to null, but due to a translation error they have been assigned values of exactly 0 in TIC v5 at MAST.

Up to date TIC information is available from the [MAST TIC documentation page](http://archive.stsci.edu/tess/tic_doc.html).