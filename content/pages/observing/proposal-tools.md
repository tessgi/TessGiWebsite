Title: Proposal and observation tools
Save_as: proposal-tools.html

[TOC]

Below we outline tools that will help the user plan their observations, and so aid with proposals.

## Target list creation
The first stop for TESS GI proposers when preparing their proposals should be the [STScI/MAST TESS pages](https://archive.stsci.edu/tess/). Here, proposers can follow tutorials to learn how to access the Target Input Catalog (TIC) and Candidate Target List (CTL), crossmatch their targets with these catalogs, and create output files with relevant target information required for the GI call. The TESS GI program office requires that if a target is in the TIC, GI proposers must provide only the following columns from the TIC in comma separated value (csv) format:

1. TIC ID (if available)
2. Right Ascension (decimal degrees)
3. Declination (decimal degrees)
4. Proper motion in Right Ascension (mas yr-1)
5. Proper motion in Declination (mas yr-1) 
6. TESS mag

Since adherence to this format is critical for target list uploads to the [Remote Proposal System](https://heasarc.gsfc.nasa.gov/ark/rps/) (RPS) website, the MAST has provided a [custom tutorial](https://archive.stsci.edu/tess/tutorials/goddard_format.html) to show GI proposers how to select and output these columns for their target lists. Please follow this tutorial to provide a compliant target list. 

In addition to the above six columns, the following additional columns can be provided as necessary (the columns order must not change):

7. Common name of target
8. Extended flag
9. Special handling flag
10. 20-second cadence flag
11. Swift time request (ksec)
12. Remarks


### TESS-point Web Tool
The [TESS-point Web Tool](https://heasarc.gsfc.nasa.gov/wsgi-scripts/TESS/TESS-point_Web_Tool/TESS-point_Web_Tool/wtv_v2.0.py) allows users to check whether a target potentially falls within the TESS field of view (FOV). In addition, the tool can be used to calculate the brightness of a target in the TESS bandpass.

The user provides the name (or TIC ID, or RA/DEC) of an object, and the tool will output which sector and camera the object is expected to be observed with (or null results if it will not fall in the TESS FOV).

For larger sets of targets, the TESS-point Web Tool will take an input file (csv) with RA and DEC (in decimal) and return the potential visibility (sector/camera) per object.

This tool can also be used to estimate the magnitude and photometric error for a point source given known magnitudes (based on the functionality of the ticgen tool, described below).

<!--
The [Web TESS Viewing (WTV) tool](https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py) developed by the TESS Science Support Center assists the community in planning and proposing.

The website implements the functionality of both [tvguide](#tvguide) and [ticgen](#ticgen) in a handy online tool.

We recommend users start by using the web-tool before experimenting with the command line tools. -->


<!--
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
-->

### ticgen
ticgen is a Python package that allows users to calculate a TESS magnitude from various other bandpasses, and calculate a 1-sigma noise level. This feature is also enabled in the [TESS-point Web Tool](https://heasarc.gsfc.nasa.gov/wsgi-scripts/TESS/TESS-point_Web_Tool/TESS-point_Web_Tool/wtv_v2.0.py). This package adds the ticgen and ticgen-csv tools to the command line.

The code and documentation is hosted on [Github](https://github.com/tessgi/ticgen) and only briefly summarized here.

 Installation:

Users will need to have a working version of Python 2 or 3 installed.
If this requirement is met, ticgen can be installed using pip:

    pip install ticgen

If you have a previous version installed, please make sure you upgrade to the latest version using:

    pip install ticgen --upgrade

It is important to upgrade frequently to ensure that you are using the most up to date TESS field parameters.

 Usage:

Installing ticgen will automatically add a command line tool to your path called *ticgen*, which takes a magnitudes as input.

For example, 

    $ ticgen -V 7.5 -J 12.0 -Ks 11.5

    TESS mag = 10.09, calculated using V/J/Ks.
    1-sigma scatter in 60 min = 212 ppm.

You can provide any combination of these magnitudes

* -T TMAG, --Tmag TMAG TESS magnitude of the source
* -J JMAG, --Jmag JMAG J magnitude of the source
* -K KSMAG, --Ksmag KSMAG Ks magnitude of the source
* -V VMAG, --Vmag VMAG V magnitude of the source
* -G GMAG, --Gmag GMAG Gaia magnitude of the source
* -H HMAG, --Hmag HMAG H magnitude of the source
* -B BMAG, --Bmag BMAG B magnitude of the source
* --Bphmag BPHMAG B photographic magnitude of the source



You can also specify the integration time in minutes. 
* -i INTEGRATION, --integration INTEGRATION
This will be used to calculate the noise. This assumes noise scales with the inverse square-root of the integration time. (default: 60)

    $ ticgen --Tmag 18.0 --integration 1440

    TESS mag = 18.00, calculated using Tmag was provided.
    1-sigma scatter in 1440 min = 51045 ppm.

You can also run this on a comma-separated variable file with magnitudes.
The header of the file must contain one or more of Tmag, Vmag, Jmag, Bmag, Bphmag, Ksmag, Hmag, and Gmag. Not all the magnitudes need to be included in the file and the columns can be in any order.

A new csv file will be created with two columns: TESS mag and 1-sigma noise level in parts-per-million.

Here is an example of an acceptable file:

    Tmag,Vmag,Jmag,Bmag,Bphmag,Ksmag,Hmag,Gmag
    12.0,,,,,,,
    ,11.5,8.1,,,6.7,,
    ,,,,,,16.0,
    ,,12.0,12.0,,8.6,,

and this would output:

    # Tmag, 1-sigma noise (ppm)
        12.000,    595.007
         9.850,    188.867
        16.700,  32331.695
        12.872,   1030.614

This code is build using the algorithms from the TESS Input Catalog publication from [Stassun et al. (2017)](https://arxiv.org/abs/1706.00495).

### [TESS-Point](https://github.com/christopherburke/tess-point)

This is a High Precision TESS pointing tool. It will convert target
coordinates given in Right Ascension and Declination to TESS detector
pixel coordinates for the [prime](primary.html) mission, [first extension](extended.html), and [second extension](second-extend.html). It can also query MAST to
obtain detector pixel coordinates for a star by TIC ID only. It provides the target ecliptic coordinates, sector number, camera number, detector number, and pixel column and row.
If there is no output, then the target is not visible to TESS.


### Filtergraph

The TESS Target Selection Working Group (TSWG) has provided a tool for GI proposers to view and manipulate the current CTL in the [Filtergraph data visualization system](https://filtergraph.com/tess_ctl) (Burger et al. 2013). Filtergraph is an online tool to upload data files, visualize the data in various formats (i.e. scatter plots, histograms, heat maps, etc.), manipulate these visualizations by filtering the data, and save figures and tables in standard image and data output formats.

The following figure provides an example of a CTL visualization that can be made using Filtergraph. The figure displays the ~400,000 highest priority stars in CTL-8 in Dec vs. RA and color-coded by T-mag. Features inherent to the CTL are immediately noticeable, such as the low density of targets in the Galactic plane (due to high background contamination and reddening), the ecliptic zone (which is not observed in the prime mission), and the higher density of targets near the ecliptic poles where TESS will have the longest continuous observation baseline and be more sensitive to transiting planets.

<br/>
<img class="img-responsive" style="max-width:87%;" src="images/giprogram/filtergraph_CTLv8.01_top_400K_stars.png">
*CTL-8 visualization generated using TIC/CTL Filtergraph portal. The
figure shows the distribution of stars in the CTL-8 in equatorial
coordinates. The color bar represents the targets' TESS
magnitudes. There are fewer stars in the Galactic plane due to
background contamination, and the ecliptic is not observed during the
prime mission. The two regions of higher target density are the
ecliptic poles, where TESS will observe continuously for nearly a
year. Image Credit: [Filtergraph](https://filtergraph.com/)*
<br/>


Additional pre-made figures are available on the CTL Filtergraph page. Users may also create their own free Filtergraph account and upload their own target lists for visualization following the instructions and tutorials on the main [Filtergraph](https://filtergraph.com/) webpage.


<!--
## Core science targets
To aid in proposal preparation we have [made a csv file available](data/core-science-targets-cycle2-v1.csv) that contains the top 100,000 priority targets in the northern ecliptic hemisphere.-->




