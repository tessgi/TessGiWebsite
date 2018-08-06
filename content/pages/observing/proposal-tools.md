Title: Proposal Tools
Save_as: proposal-tools.html

[TOC]

We have developed two pieces of softare to aid in the development of proposals. [TVGuide](#tvguide) helps with determining whether are target is observable in Cycle 1, and [ticgen](#ticgen) is used to calculate the brightness of a target in the TESS bandpass. In addition, resources have been created by various other team to aid in writing proposals.

We have [created a webtool](https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py) that implements the functionality of ticgen and tvguide. This is our recommended avenue to accessing these utilities.

## Target list creation
The first stop for TESS GI proposers when preparing their proposals should be the [STScI/MAST TESS pages](https://archive.stsci.edu/tess/). Here, proposers can follow tutorials to learn how to access the Target Input Catalog (TIC) and Candidate Target List (CTL), crossmatch their targets with these catalogs, and create output files with relevant target information required for the GI call. The TESS GI program office requires that if a target is in the TIC, GI proposers must provide only the following columns from the TIC in comma separated value (csv) format:

1. TIC ID (if available)
2. Right Ascension (decimal degrees)
3. Declination (decimal degrees)
4. Proper motion in Right Ascension (mas yr-1)
5. Proper motion in Declination (mas yr-1) 
6. TESS mag

Since adherence to this format is critical for target list uploads to the [Remote Proposal System](https://heasarc.gsfc.nasa.gov/ark/rps/) (RPS) website, the MAST has provided a [custom tutorial](https://archive.stsci.edu/tess/tutorials/goddard_format.html) to show GI proposers how to select and output these columns for their target lists. Please follow this tutorial to provide a compliant target list. 


## Filtergraph

The Target Selection Working Group (TSWG) has also provided a tool for GI proposers to view and manipulate a high-priority subset of the current CTL in the [Filtergraph data visualization system](https://filtergraph.com/tess_ctl) (Burger et al. 2013). Filtergraph is an online tool to upload data files, visualize the data in various formats (i.e. scatter plots, histograms, heat maps, etc.), manipulate these visualizations by filtering the data, and save figures in standard image output formats. 

The following figure provides an example of a CTL visualization that can be made using Filtergraph. The figure displays all stars in CTL-5 in Dec vs. RA and color-coded by T mag. Features inherent to the CTL are immediately noticeable, such as the lower density of targets in the Galactic plane (due to high background contamination) and the higher density of targets in the ecliptic poles where TESS will have the longest continuous observation baseline and be more sensitive to transiting planets. 
<br/>
<img class="img-responsive" style="max-width:67%;" src="images/giprogram/filtergraph.png">
* CTL-5 visualization generated using TIC/CTL Filtergraph portal. The figure shows the distribution of stars in the CTL-5 in equatorial coordinates. The color bar represents the targets' TESS magnitudes. There are fewer stars in the Galactic plane due to background contamination. The two elliptical regions of higher target density are the ecliptic poles, where TESS will observe continuously for nearly a year. Image Credit: [Filtergraph](https://filtergraph.com/)*
<br/>


Additional premade figures are available on the CTL Filtergraph page, including CTL TESS mag and effective temperature histograms. Users may also create their own Filtergraph account and upload their own target lists for visualization following the instructions and tutorials on the main [Filtergraph](https://filtergraph.com/) webpage. 

## Web TESS Target Tool
The [Web TESS Target Tool](https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py) provided by the TESS Science Support Center assists the community in planning and proposing. The website implements the functionality of both [tvguide](#tvguide) and [ticgen](#ticgen) in a handy online tool.

We recommend users start by using the webtool before experimenting with the command line tools.

## TVGuide
TVGuide is a Python package that allows users to check whether a target potentially falls within the field of view of TESS.

In particular, the package adds the tvguide and tvguide-csv tools to the command line, which allow the visibility of targets to be checked during Cycle 1.

The code and documentation is hosted on [Github](https://github.com/tessgi/tvguide) and only briefly summarized here.

### Installation

Users will need to have a working version of Python 2 or 3 installed.
If this requirement is met, tvguide can be installed using pip:

    pip install tvguide

If you have a previous version installed, please make sure you upgrade to the latest version using:

    pip install tvguide --upgrade

It is important to upgrade frequently to ensure that you are using the most up to date TESS field parameters.

### Usage

Installing tvguide will automatically add a command line tool to your path called *tvguide*, which takes a target as input and writes a new list that indicates the observability of the target, i.e. whether or not might fall on one of the detectors of the spacecraft's focal plane.

For example, 

    tvguide 219.9009 -60.8356

    Success! The target may be observable by TESS during Cycle 1.
    We can observe this source for:
    maximum: 2 sectors
    minimum: 0 sectors
    median:  1 sectors
    average: 1.16 sectors

You can also run on a file with targets currently implemented is using RA and Dec.

    tvguide-csv inputfilename.csv

This will return a file with the two original columns plus two additional columns giving the minimum number and maximum of sectors that the target will be observed by with TESS.


## ticgen
TVGuide is a Python package that allows users calculate a TESS magnitude from various other bandpasses, and calculate a 1-sigma noise level

In particular, the package adds the ticgen and ticgen-csv tools to the command line.

The code and documentation is hosted on [Github](https://github.com/tessgi/ticgen) and only briefly summarized here.

### Installation

Users will need to have a working version of Python 2 or 3 installed.
If this requirement is met, tvguide can be installed using pip:

    pip install ticgen

If you have a previous version installed, please make sure you upgrade to the latest version using:

    pip install ticgen --upgrade

It is important to upgrade frequently to ensure that you are using the most up to date TESS field parameters.

### Usage

Installing ticgen will automatically add a command line tool to your path called *ticgen*, which takes a magnitudes as input.

For example, 

    $ ticgen -V 7.5 -J 12.0 -Ks 11.5

    TESS mag = 10.09, calculated using V/J/Ks.
    1-sigma scatter in 60 min = 212 ppm.

You can provide any combination of these mangitudes

* -T TMAG, --Tmag TMAG TESS magnitude of the source
* -J JMAG, --Jmag JMAG J magnitude of the source
* -K KSMAG, --Ksmag KSMAG Ks magnitude of the source
* -V VMAG, --Vmag VMAG V magnitude of the source
* -G GMAG, --Gmag GMAG Gaia magnitude of the source
* -H HMAG, --Hmag HMAG H magnitude of the source
* -B BMAG, --Bmag BMAG B magnitude of the source
* --Bphmag BPHMAG B photgraphic magnitude of the source



You can also specify the integration time in minutes. 
* -i INTEGRATION, --integration INTEGRATION
This will be used to calculate the noise. This assumes noise scales with the inverse square-root of the integration time. (default: 60)

    $ ticgen --Tmag 18.0 --integration 1440

    TESS mag = 18.00, calculated using Tmag was provided.
    1-sigma scatter in 1440 min = 51045 ppm.

You can also run on a comma-seperated variable file with magnitudes.
The header of the file must contain one or more of Tmag, Vmag, Jmag, Bmag, Bphmag, Ksmag, Hmag, and Gmag. Not all the magnitues need to be included in the file and the columns can be in any order.

A new csv file will be created with two columns: TESS mag and 1-sigma noise level in parts-per-million.

Here is an example of an acceptable file

    Tmag,Vmag,Jmag,Bmag,Bphmag,Ksmag,Hmag,Gmag
    12.0,,,,,,,
    ,11.5,8.1,,,6.7,,
    ,,,,,,16.0,
    ,,12.0,12.0,,8.6,,

and this would output

    # Tmag, 1-sigma noise (ppm)
        12.000,    595.007
         9.850,    188.867
        16.700,  32331.695
        12.872,   1030.614

This code is build using the algorithms from the TESS Input Catalog publication from [Stassun et al. (2017)](https://arxiv.org/abs/1706.00495).

## Core science targets
This isn't software, but to aid in proposal preparation we have [made a csv file available](data/core-science-targets-v2.csv) that contains the top 100,000 priority targets in the southern ecliptic hemisphere.


# Proposal templates
We have made available proposal templates to aid users in writing GI proposals. Use of these templates is not required. 

* [MS Word](docs/tessgi_template.docx)
* [Latex](docs/tessgi_template.tex)
* [PDF](docs/tessgi_template.pdf)

