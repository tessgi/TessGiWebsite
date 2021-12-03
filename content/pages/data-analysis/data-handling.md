Title: TESS data processing pipeline
Save_as: data-handling.html

[TOC]

The flow of data from the spacecraft to its final archive involves participation from multiple institutions that make up the TESS project team.
The TESS data processing pipeline itself was developed by the Science Processing Operations Center (SPOC) at NASA Ames Research Center and builds on the legacy of the Kepler data processing pipeline. A brief overview of how TESS data is handled and the pipeline is presented below, more details can be found in the SPOC paper available in the [documentation page](documentation.html).

## Pipeline overview

<br/>
<img class="img-responsive" style="max-width:75%;" src="images/mission/tess_operations2.png">
<br/>

Data from the TESS spacecraft are downloaded through the Deep Space Network (DSN) and delivered to the Payload Operations Center (POC) at the [Massachusetts Institute ofTechnology](https://tess.mit.edu) (MIT). 

The POC sends uncalibrated requantized pixel data, target lists, spacecraft configuration and engineering data, and focal plane characterization models (for calibration) to the Science Processing Operations Center (SPOC) at [NASA Ames](https://www.nasa.gov/ames/tess-pipeline).

The SPOC calibrates the science data in two steps, first by the orbit and then by the sector. The SPOC uses instrument calibration models provided by the POC to calibrate all science data. Once a full sector is calibrated the transiting planet search software is run by the SPOC to identify and flag threshold crossing events (TCEs). Calibrated target pixels and FFIs, light curves generated from 20-sec and  2-min cadence targets, and TCEs are sent to the TESS Science Office (TSO, which includes MIT and the Smithsonian Astrophysical Observatory, SAO).

The TSO is responsible for detailed analysis of TCEs and the identification of TESS Objects of Interest (TOIs). The TSO delivers the lists of TOIs to the [Mikulski Archive for Space Telescopes](https://archive.stsci.edu/tess/) (MAST, located at the Space Telescope Science Institute, STScI) along with dispositions and information documenting the vetting process for each TOI on a regular schedule, nominally every four months.

The processed data and meta-data from the SPOC are archived at MAST. MAST is the primary science data archive for TESS and provides tools to search and retrieve data. The TESS Science Support Center operates the Guest Investigator (GI) Program, which supplies a list of GI targets to the POC, and the GI proposers may retrieve their data from the MAST. All data archived at MAST has no proprietary period and is publicly available.

The Full Frame Images (FFIs), which are calibrated by the SPOC, were collected at a 30 min cadence in the [primary mission](primary.html), 10 min in the [first extension](extend.html), and 200 sec in the [second extension](second-extended.html). There is a fast turn-around time for processing the science data, a high on-board storage capacity for TESS ~192 GB, and a high data rate since TESS's orbit is closer to Earth. All of the data is processed on the NASA Advanced Supercomputing (NAS) Division's Pleiades supercomputer.

## Pipeline products

The SPOC pipeline products include:

* Target Pixel files (raw and calibrated pixel data)
* Target Light Curve files (photometric analysis and systematic error-corrected time series data)
* FFI files (raw, calibrated, and uncertainty images of the CCDs)
* Collateral Pixel files (raw and calibrated collateral pixel data)
* Data validation products
* Ancillary files that include pipeline meta-data and co-trending basis vectors (CBVs)

SPOC products are archived at the Mikulski Archive for Space Telescopes (MAST). There is no proprietary data period for any TESS data products. Further information on the data products and how to access them can be found on the [data products](data-products.html) and [data access](data-access.html) page.



