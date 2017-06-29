Title: Proposal Tools
Save_as: proposal-tools.html

[TOC]

We have developed two pieces of softare to aid in the developement of proposals. [TVGuide](#tvguide) helps with determining whether are target is observable in Cycle 1, and [ticgen](#ticgen) is used to calculate the brightness of a target in the TESS bandpass. 

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
Will be added shortly.

