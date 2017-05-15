Title: Accessing TESS data products
Save_as: data-access.html

[TOC]

The *official* archive for TESS mission data products is the
[Mikulski Archive for Space Telescopes (MAST)](https://archive.stsci.edu/tess)
which is hosted at the
[Space Telescope Science Institute (STScI)](http://www.stsci.edu/). 

In the following sections we list the main products from TESS, and we describe a few of the products in some detail.  For tools
and tips on
inspecting and analyzing TESS data, [users should check out this page](software.html).

We encourage users of TESS data to read through the
(documentation associated with the TESS data products)[documentation.html]. The first port of call for the TESS user is the [TESS Observatory Handbook](link!!). 




<!-- There is documentation specific to the [TESS data products](https://archive.stsci.edu/kepler/data_products.html). Additional documentation can be found
[here](https://archive.stsci.edu/kepler/documents.html) or can be downloaded directly by following the links
below.

* [Kepler Archive Manual](http://archive.stsci.edu/kepler/manuals/archive_manual.pdf)
* [Kepler Instrument Handbook](data/documentation/KSCI-19033-001.pdf) and [Supplement](data/documentation/KSCI-19033-001_supplement.tar)
* [Kepler Input Catalog (KIC)](http://adsabs.harvard.edu/abs/2011AJ....142..112B)
* [Kepler Data Characteristics Handbook](http://archive.stsci.edu/kepler/manuals/Data_Characteristics.pdf)
* [Kepler Data Processing Handbook](http://archive.stsci.edu/kepler/manuals/KSCI-19081-001_Data_Processing_Handbook.pdf)
* [Kepler Data Release Notes](data-products.html#kepler-data-release-notes) 
<br/>
* [K2 Ecliptic Plane Input Catalog (EPIC)](https://archive.stsci.edu/k2/epic.pdf)
* [K2 Data Release Notes](data-products.html#k2-data-release-notes)
 -->
## TESS product overview

The [TESS mission page at MAST](https://archive.stsci.edu/tess/) contains the latest news and updates
on TESS products. The following TESS data products and catalogs will be available
through MAST:

**Data products at MAST**

* Two-minute cadence target pixel files
* Two-minute cadence light curves
<!-- * Data validation time series files
* Full frame images (calibrated and uncertainty files)
* Cotrending basis vectors files
* Simulated Data files
* Artifact removal pixel files
* Background pixel files
* Collateral files
* Reverse clock files
* Ancillary engineering files
* Latest SPICE kernels (bsp and tsc binary files) -->

**Catalogs at MAST**

* TESS Input Catalog (TIC)
* Candidate Target List (CTL)
<!-- * Revised stellar parameters of Kepler targets (Q1-Q16)
* Revised stellar parameters of Kepler targets (Q1-Q17)
* Kepler Objects of Interest (KOI)
* Kepler/GALEX cross match catalog
* False positive working group tables -->
* Observed targets by quarter

<!-- The
[Kepler mission page at NExScI](http://exoplanetarchive.ipac.caltech.edu/docs/KeplerMission.html)
contains the following products and also details the instructions for
requesting a Kepler number for new planets discovered in the
Kepler data:

**Data products at NExScI**

* KOI activity tables
* Threshold-crossing events and data validation tables
* Stellar information for observed Kepler targets
* Ccompleteness and reliability products -->


## Main data products

A few of the data products from TESS are described
below. For a comprehensive list of available products.

### Full frame images (FFIs)

Describe...

<br/>

<img class="img-responsive" style="min-width:97%;" src="images/mission/tess_observingsectorschematic_Winnpresentation.jpg">

<br/>

### Target pixel files (TPFs)
Describe...

The image is a Kepler TPF for now.

<br/>

<img class="img-responsive" style="min-width:97%;" src="images/data/TPF-FV3.jpg">

<br/>



### Light curve files



### Collateral data



## Auxiliary data products


### Cotrending basis vectors (CBVs)

CBVs will be provided for each operational sector of the mission. These are derived by
the TESS pipeline from a Principle Component Analysis and used to
mitigate for systematic artifacts within the the target light
curves. If TESS users see residual systematic problems
within their light curve data, the CBVs can be employed in performing
a manual photometric correction, more tailored towards the users
science. 

### Pixel response functions (PRFs)


### Simualted Data
