Title: Sector 75
Save_as: sector_75.html

[TOC]

TIC ID's that had issues in Sector 75.

##Targets not processed in 2-min pipeline and so missing a light curve:
99843265, 164642404, 229540730, 232853959, 1961255595

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
123446661, 165602023, 198242676, 229540730, 229686919, 229686929, 233185267, 253043596, 341873045, 378268070, 1551711135, 1961255595

##Targets with aperture warnings in 20-sec data: 
165602023, 253043596, 341873045

Warnings during
aperture assignment occur when the aperture is discontinuous or clipped, and the resulting
photometry is expected to be unreliable.