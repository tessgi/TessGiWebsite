Title: TESS data processing pipeline
Save_as: pipeline.html

[TOC]

The TESS data processing pipeline is currently being developed by the Science Processing Operations Center (SPOC) at NASA Ames Research Center and builds on the legacy of the Kepler data processing pipeline. A brief overview is presented below, and more details can be found in the SPOC paper available in the [documentation](documentation.html) page.

## Pipeline overview

The SPOC will receive raw data via the Payload Operations Center (POC) at MIT. The SPOC pipeline processes the raw pixels, extracts photometry and astrometry for each target star, identifies and removes systematic errors, flags transiting planet signatures, and performs a suite of diagnostic tests. Many software modules developed for Kepler have significant overlap with what is needed to process TESS data. 

One of the primary differences between TESS and Kepler pipeline processing is the volume of data that TESS will produce over the course of the 2 year nominal mission. TESS science data have a nominal cadence of 2 min compared to 29.4 min for Kepler. The Full Frame Images (FFIs), which will be calibrated by the SPOC, are collected at 30 min cadence compared to Kepler's monthly FFIs. Furthermore, there will be a faster turn-around time for processing the science data (27.4 days for TESS vs. 120 days for Kepler), a higher on-board storage capacity for TESS (192 GB vs. 17 GB), and a much higher data rate since  TESS' orbit is closer to Earth. All of these factors introduce new challenges to pipeline processing, which (like Kepler) will be processed on the NASA Advanced Supercomputing (NAS) Division's Pleiades supercomputer.



## Pipeline products

The SPOC pipeline products include:

* Target Pixel files (raw and calibrated pixel data)
* Target Light Curve files (photometric analysis and systematic error-corrected time series data)
* FFI files (raw, calibrated, and uncertainty images of the CCDs)
* Collateral Pixel files (raw and calibrated collateral pixel data)
* Data validation products
* Ancillary files that include pipeline meta-data and co-trending basis vectors (CBVs)

SPOC products will be archived to the Mikulski Archive for Space Telescopes (MAST). There is no proprietary data period for any TESS data products.


