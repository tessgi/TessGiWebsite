Title: Sector 3
Save_as: sector_3.html

[TOC]

TIC ID's that had issues in Sector 3.

##Targets not processed in 2-min pipeline:
 38877693, 114434141, and 238196512.

##Targets placed on the wrong CCD in Camera 4:
260192532, 150065151, 150106553, and 141423536
No optimal apertures or light curves were produced

##Blended stars:
300015238  with 300015239

A star is considered to be bended when its flux has been significantly contaminated by a nearby bright star(s). Since the contaminating flux is considered very large, the resulting photometry for such targets is expected to be unreliable.

##Not capturing bleed trails:
220393543

Targets with pixel stamps that did not fully capture the bleed trails.

##Target offset:
29928567 was selected by a GI program with a proper motion override. The RA/Dec proper motion was set to 3321.0/562.0 mas/year (the TIC lists the RA/Dec proper motion as 0.0/0.0 mas/year). However, this change was not propagated to the SPOC pipeline, and the calculated optimal aperture is therefore offset from the source by several pixels. The target is correctly centered in the target pixel file, but the light curve file does not contain measurements from this source because of the aperture shift.