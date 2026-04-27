# 2D projector trained on enamine hit locator

This model uses lazy-chemvis tool to performs PCA, UMAP, t-SNE and TMAP projections taking the Enamine Hit Locator library with 416K compounds as a chemical space of reference. ECFP4 fingerprints (2048 bits) and RDKit physicochemical descriptors are used as molecular descriptors. Two coordinates are returned for each projection method.

This model was incorporated on 2026-03-20.Last packaged on 2026-04-27.

## Information
### Identifiers
- **Ersilia Identifier:** `eos45di`
- **Slug:** `lazychemvis-enamine-hl`

### Domain
- **Task:** `Representation`
- **Subtask:** `Projection`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `8`
- **Output Consistency:** `Fixed`
- **Interpretation:** Coordinates of 2D projections, namely PCA, UMAP, tSNE and TMAP.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| pca_x | float |  | First principal component projected on the reference chemical space |
| pca_y | float |  | Second principal component projected on the reference chemical space |
| tmap_x | float |  | First TMAP dimension projected on the reference chemical space |
| tmap_y | float |  | Second TMAP dimension projected on the reference chemical space |
| tsne_x | float |  | First TSNE dimension projected on the reference chemical space |
| tsne_y | float |  | Second TSNE dimension projected on the reference chemical space |
| umap_x | float |  | First UMAP dimension projected on the reference chemical space |
| umap_y | float |  | Second UMAP dimension projected on the reference chemical space |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos45di](https://hub.docker.com/r/ersiliaos/eos45di)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos45di.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos45di.zip)

### Resource Consumption
- **Model Size (Mb):** `1007`
- **Environment Size (Mb):** `8082`
- **Image Size (Mb):** `11031.33`

**Computational Performance (seconds):**
- 10 inputs: `39.77`
- 100 inputs: `109.52`
- 10000 inputs: `-1`

### References
- **Source Code**: [https://github.com/ersilia-os/lazy-chemvis](https://github.com/ersilia-os/lazy-chemvis)
- **Publication**: [https://github.com/ersilia-os/lazy-chemvis](https://github.com/ersilia-os/lazy-chemvis)
- **Publication Type:** `Other`
- **Publication Year:** `2026`
- **Ersilia Contributor:** [Marina18](https://github.com/Marina18)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos45di
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos45di
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
