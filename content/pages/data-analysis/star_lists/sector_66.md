Title: Sector 66
Save_as: sector_66.html

[TOC]

TIC ID's that had issues in Sector 66.

##Targets not processed in 20-sec pipeline and so missing a light curve:
341149986

##Targets not processed in 2-min pipeline and so missing a light curve:
38877693, 57334718, 191437754, 238196512, 255559489, 262834160, 325635393, 341149986, 364216056

For targets that were not processed with the photometric pipeline, the target pixel files
with original and calibrated pixel data are provided, but no light curves are produced. Note
that the target pixel files do not include a background correction for stars without light
curves. The most common reason for a target to not be processed with the photometric
pipeline is that the target exceeds a brightness threshold (Tmag ≲ 1.8) that results in
large pixel stamps. A target located too close to a very bright star, having a comparably
bright companion, impacted by saturated star bleed trails, or having an error in identifying
a clean background region are less common causes for a target to not be processed with
the photometric pipeline. Visual examination of the target along with custom aperture
selection may be needed for photometric analysis of the impacted targets.

##Targets with aperture warnings in 2-min data: 
171207618, 220393543, 238092498, 300015238, 340411626, 384196595, 384196633, 420967314, 1698462156

Warnings during
aperture assignment occur when the aperture is discontinuous or clipped, and the resulting
photometry is expected to be unreliable.