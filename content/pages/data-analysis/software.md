Title: TESS Software Tools
Save_as: software.html

[TOC]

<!-- ## Overview -->
## Observation planning

* Web TESS Viewing Tool
The [Web TESS Viewing (WTV) tool](https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py) allows users to check whether a target potentially falls within the TESS field of view (FOV). In addition, WTV can be used to calculate the brightness of a target in the TESS bandpass.

See our [proposal tools page](proposal-tools.html) for additional resources that aid in the preparation of GI proposals:


## TESS Data analysis

### [lightkurve](http://lightkurve.keplerscience.org)
Lightkurve is a python-based package developed by the Kepler Guest Observer’s office for use by the community to work with Kepler and K2 data. The TESS GI Office has partnered with the Kepler GO Office to develop lightkurve for use with TESS data. 

Lighkurve functionality:

* Reading, writing, and interacting with pipeline products (TPFs, LightCurve files, etc) 
* Extracting lightcurves from pixels using custom aperture photometry or custom PSF fitting. 
* Removing trends or correcting systematics using widely-used, non-controversial methods (SavGol, CBVs, SFF, ...)

The lightkurve git repository is [here](https://github.com/KeplerGO/lightkurve).


<!--
1) Add a basic BLS interface and tutorials (cf. https://github.com/astropy/astropy/pull/7391 )
2) Add basic seismology tools and tutorials (cf. https://github.com/KeplerGO/lightkurve/issues/114 )
3) Add interactive data inspection widgets (cf. https://github.com/KeplerGO/lightkurve/pull/100 )
-->



## Tutorials

STScI [Notebooks](https://github.com/spacetelescope/notebooks/tree/master/notebooks/MAST/TESS)



# Kepler and K2 tools

Many tools and software were developed for the Kepler Mission, and Kepler’s extended mission K2. Kepler and K2 had three data modes: long cadence (30 min) and short cadence (1 min) postage stamps, and quarterly FFIs (30 min). TESS has two data modes, short cadence (2 min) postage stamps and 30 min cadence FFIs. The data formats, target pixel files (TPF) and full frame images (FFIs) are similar for Kepler/K2 and TESS.


## Detrending and analysis


* [PyKE suite](http://pyke.keplerscience.org)

The PyKE tools developed for the Kepler mission. The git repository can be found [here](https://github.com/KeplerGO/PyKE)

* [EVEREST](https://github.com/rodluger/everest)

EPIC Variability Extraction and Removal for Exoplanet Science Targets; Detrending of K2 light curves

* [k2sc](https://github.com/OxES/k2sc)

K2 systematics correction via simultaneous modelling of stellar variability and jitter-dependent systematics using Gaussian Process regression


* [nutella](https://github.com/benmontet/nutella)

Point spreads for Kepler/K2 inference

* [skope](https://github.com/nksaunders/skope)

Synthetic K2 objects for PLD experimentation

* [k2phot](https://github.com/petigura/k2phot)

Routines for extracting lightcurves from K2 images

* [K2-CPM](https://github.com/jvc2688/K2-CPM)

K2 Causal Pixel Model

* [halophot](https://github.com/hvidy/halophot/)

K2 Halo Photometry for very bright stars

* [cave](https://github.com/nksaunders/cave)

Crowded Aperture Variability Extraction

* [celerite-asteroseis](https://github.com/skgrunblatt/celerite-asteroseis)

Transit fitting and basic time-domain asteroseismology using celerite and ktransit

* [k2photometry](https://github.com/vincentvaneylen/k2photometry)

Read, reduce and detrend K2 photometry and search for transiting planets

* [keplersmear](https://github.com/benjaminpope/keplersmear)

Make light curves from Kepler and K2 collateral data

* [OxKeplerSC](https://github.com/OxES/OxKeplerSC)

Kepler jump and systematics correction using Variational Bayes and shrinkage priors.

* [K2Pipeline](https://github.com/FGCUStellarResearch/K2Pipeline)

Data reduction and detrending pipeline for K2 data in Matlab

* [PySysRem](https://github.com/stephtdouglas/PySysRem)

Correct systematic effects in large set of photometric light curves

* [astrobase](https://github.com/waqasbhatti/astrobase)

lightcurve tools: periodograms (BLS, Lomb-Scargle, analysis of variance), simple detrending (AKA: fit high order polynomials), light-curve math: phase-folding, binning. Also, a server for vetting.
Tutorial [here](github.com/waqasbhatti/astrobase-notebooks)



## Full frame images

* [f3](https://github.com/benmontet/f3)

Full Frame Fotometry from the Kepler Full Frame Images

* [DIA](https://github.com/ryanoelkers/DIA)

Difference Imagine Analysis to extract a light curve from FFIs

* TESSCut(coming soon)

* [FFIorBUST](https://github.com/jradavenport/FFIorBUST)

Make light curves from the Kepler Full Frame Images

* [Lightkurve](http://lightkurve.keplerscience.org)

Extract light curves from FFIs, package into TPFs

* [kepcal](https://github.com/dfm/kepcal)

Self calibration using the Kepler FFIs

* [SpyFFI](https://github.com/zkbt/spyffi)

Tools for simulating TESS imaging at multiple cadences, including cartoon light curves + jitter + focus drifts, cosmic rays

* [ISIS](http://www2.iap.fr/users/alard/package.html)

Process CCD images using image subtraction

* [HOTPANTS](http://web.ipac.caltech.edu/staff/fmasci/home/astro_refs/HOTPANTSsw2011.pdf)

High Order Transform of PSF and Template Subtraction; Similar method, but improvement on ISIS image subtraction processing. Doc for HOTPANTS [here](http://adsabs.harvard.edu/abs/2015ascl.soft04004B).



## Positional

* [k2fov](https://github.com/KeplerGO/K2fov)

Check whether targets are in K2 FOV 

* [k2ephem](https://github.com/KeplerGO/K2ephem)

Check whether a Solar System body is (or was) observable by K2 

* [k2-pix](https://github.com/stephtdouglas/k2-pix)

Overlay a sky survey image on a K2 target pixel stamp 

* [k2flix](https://github.com/barentsen/k2flix)

Create quicklook movies from the pixel data observed by Kepler/K2/TESS 

* [k2mosaic](https://github.com/barentsen/k2mosaic)

Mosaic Target Pixel Files (TPFs) obtained by Kepler/K2 into images and movies 

* [tvguide](https://github.com/tessgi/tvguide)

A tool for determining whether stars and galaxies are observable by TESS. 

* [tess-point](https://github.com/christopherburke/tess-point)


## Data access

* [kplr](https://github.com/dfm/kplr)

Tools for working with Kepler data using Python 

* [k2plr](https://github.com/rodluger/k2plr)

Fork of dfm/kplr with added k2 functionality 

* [kepFGS}(https://github.com/christinahedges/kepFGS)

Tools to use the Kepler and K2 Fine Guidance Sensor data 




## Meta data


* [kadenza](https://github.com/KeplerGO/kadenza)

Converts raw cadence target data from the Kepler space telescope into FITS files 

* [k2-quality-control](https://github.com/KeplerGO/k2-quality-control)

Automated quality control of Kepler/K2 data products 

* [SuperstampFITS](https://github.com/amcody/SuperstampFITS)

Create individual FITS files of K2 superstamp regions 

* [keputils](https://github.com/timothydmorton/keputils)

Basic module for interaction with KOI and Kepler-stellar tables 


## Planet search


* [PyTransit](https://github.com/hpparvi/PyTransit)

Fast and easy transit light curve modeling using Python and Fortran 

* [batman](https://github.com/lkreidberg/batman)

Fast transit light curves models in Python 

* [ktransit](https://github.com/mrtommyb/ktransit)

A simple exoplanet transit modeling tool in python 

* [planetplanet](https://github.com/rodluger/planetplanet)

A general photodynamical code for exoplanet light curves 

* [ketu](https://github.com/dfm/ketu)

A search for transiting planets in K2 data 

* [ttvfast-python](https://github.com/mindriot101/ttvfast-python)

Python interface to the TTVFast library 

* [terra](https://github.com/petigura/terra)

Transit detection code 

* [pysyzygy](https://github.com/rodluger/pysyzygy)

A fast and general planet transit (syzygy) code written in C and in Python 

* [k2ps](https://github.com/hpparvi/k2ps)

K2 planet search 

* [lcps](https://github.com/matiscke/lcps)

A tool for pre-selecting light curves with possible transit signatures 


## Vetting


* [DAVE](https://github.com/barentsen/dave)

Discovery And Vetting of K2 Exoplanets 


## Population statistics

* [VESPA](https://github.com/timothydmorton/VESPA)

Calculating false positive probabilities for transit signals 

* [kepler-robovetter](https://github.com/nasa/kepler-robovetter)

The Kepler prime robovetter 

* [koi-fpp](https://github.com/timothydmorton/koi-fpp)

False positive probabilities for all KOIs 

* [KeplerPORTS](https://github.com/nasa/KeplerPORTS)

The Kepler pipeline 

* [Kepler-FLTI](https://github.com/nasa/Kepler-FLTI)

Kepler Prime Flux-Level Transit Injection 





## Science




* [isochrones](https://github.com/timothydmorton/isochrones)

Pythonic stellar model grid access; easy MCMC fitting of stellar properties 

* [ldtk](https://github.com/hpparvi/ldtk)

Python toolkit for calculating stellar limb darkening profiles 

* [isoclassify](https://github.com/danxhuber/isoclassify)

Perform stellar classifications using isochrone grids 

* [appaloosa](https://github.com/jradavenport/appaloosa)

Python-based flare finding code for Kepler light curves 

* [pymacula](https://github.com/timothydmorton/pymacula)

Python wrapper for Macula analytic starspot code 

* [MulensModel](https://github.com/rpoleski/MulensModel)

Microlensing Modelling package 

* [animate_spots](https://github.com/stephtdouglas/animate_spots)

Make frames for animated gifs/movies showing a rotating spotted star 

* [decatur](https://github.com/jadilia/decatur)

Tidal synchronization of Kepler eclipsing binaries 

* [FoFreeAST](https://github.com/skgrunblatt/FoFreeAST)

Fourier-free Asteroseismology: uses celerite to model granulation and oscillations of stars 




## Other


* [limb darkening](https://arxiv.org/abs/1804.10295)

Limb-darkening and gravity-darkening coeffts for TESS

* [PandExo](https://github.com/natashabatalha/PandExo)

A community tool for transiting exoplanets with JWST & HST 

* [kepler_orrery](https://github.com/ethankruse/kepler_orrery)

Make a Kepler orrery gif or movie of all the Kepler multi-planet systems 

* [radvel](https://github.com/California-Planet-Search/radvel)

General toolkit for modeling radial velocity data 

* [PyOrbit](https://github.com/LucaMalavolta/PyORBIT)

Simultaneously characterize the orbits of exoplanets and the noise induced by stellar activity. 



<!--
## Observation planning
We currently have two piece of software available to assist with writing proposals: [tvguide](proposal-tools.html#tvguide) and [ticgen](proposal-tools.html#ticgen). These tools are described in our [proposal tools page](proposal-tools.html). We also have a [web tool](https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py) that provides this functionality.


## Data analysis
The TESS Science Support Center will be providing software to analyze TESS data. This will be built upon the PyKE software created by the [Kepler Science Center](https://keplerscience.arc.nasa.gov).

MAST will be providing open-source, Python software that will allow users to create custom cutouts of TESS Full-Frame Images given a
coordinate and area on the sky. The software will provide cutouts of each 30-minute FFI in target pixel file (TPF) FITS format. There are plans to offer additional functionality, such as quick-look light curves from the cutouts, and source catalogs that can be overlaid on the returned files.


* Tutorials
We will be creating tutorials to assist with using the available software. -->