Title: Sector 72
Save_as: sector_72.html

[TOC]

TIC ID's that had issues in Sector 72.

##Targets not processed in 2-min pipeline and so missing a light curve:
95431294, 117355623, 184842717, 357348164, 423088367 

##Targets not processed in 20-sec pipeline and so missing a light curve:
184842717

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
27550294, 117355623, 184842717, 350347140, 357348164, 800823400, 903126673

##Targets with aperture warnings in 20-sec data: 
184842717, 350347140

Warnings during
aperture assignment occur when the aperture is discontinuous or clipped, and the resulting
photometry is expected to be unreliable.