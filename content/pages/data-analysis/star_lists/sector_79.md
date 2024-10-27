Title: Sector 79
Save_as: sector_79.html

[TOC]

TIC ID's that had issues in Sector 79.

##Targets not processed in 2-min pipeline and so missing a light curve:
154699609,
255909448,
303256075,
329269366,
518659900

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
198242676,
258873063,
284183146,
303256075,
329269366,
367912480,
394130313,
424429430,
441804565,
461523884,
461632414,
518659900,
1308480726,
1400086045

Warnings during
aperture assignment occur when the aperture is discontinuous or clipped, and the resulting
photometry is expected to be unreliable.