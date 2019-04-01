[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/fadymedhat/YorNoise-for-MCLNN/blob/master/LICENSE)

# YorNoise dataset for MCLNN

The [YorNoise](https://github.com/fadymedhat/YorNoise) environmental sound dataset.

| Clip Duration  | Format | Count | Categories|
|:---:|:---:|:---:|:---:|
| 4 secs | .wav | 1527 | 2 |

Dataset Summary:
 * Clips are 4-seconds in length with 44100 Hz sampling rates.
 * The dataset is released into predefined 10-fold splits for cross-validation.
 * It is combined through the experiments with the [UrbanSound8k](https://urbansounddataset.weebly.com/urbansound8k.html) dataset to form a 12-classes dataset.  

 
 This folder contains:
  * Scripts required to prepare the UrbanSound8k dataset for the MCLNN processing.
  * Pretrained weights and indices for the 10-fold cross-validation in addition to the standardization parameters 
  to replicate the results in:
 
    _Fady Medhat, David Chesmore and John Robinson, "Recognition of Acoustic Events Using Masked Conditional Neural Networks," 2017 16th IEEE International Conference on Machine Learning and Applications (ICMLA)_
 
 ## Prepossessing
 
The preprocessing involved in preparing the YorNoise dataset is resampling to 22050 Hz.

#### Preparation scripts prerequisites

The [preparation scripts](https://github.com/fadymedhat/YorNoise-for-MCLNN/tree/master/YorNoise_preparation_scripts) require the following packages to be installed beforehand:
   * [ffmpeg](https://www.ffmpeg.org/) version N-81489-ga37e6dd
   * numpy 1.11.2+mkl
   * librosa 0.4.0
   * h5py 2.6.0yornoise_storage_ordering.txt
 
#### Steps
1. Download the [UrbanSound8k](https://urbansounddataset.weebly.com/urbansound8k.html) and execute its preprocessing scripts in the [preparation scripts](https://github.com/fadymedhat/UrbanSound8K-for-MCLNN/tree/master/UrbanSound8K_preparation_scripts) following the order of their labels.
1. Download the [YorNoise](https://github.com/fadymedhat/YorNoise) dataset and execute the scripts in the [preparation scripts](https://github.com/fadymedhat/YorNoise-for-MCLNN/tree/master/YorNoise_preparation_scripts) following the order of their labels.
2. Make sure the files are ordered following the [YorNoise_storage_ordering](https://github.com/fadymedhat/YorNoise-for-MCLNN/blob/master/yornoise_storage_ordering.txt) file.
3. Configure the spectrogram transformation within the [Dataset Transformer](https://github.com/fadymedhat/MCLNN/tree/master/dataset_transformer) and generate the MCLNN-Ready hdf5 for the dataset using the [YorNoiseUrbansound8k_MCLNN.csv](https://github.com/fadymedhat/YorNoise-for-MCLNN/blob/master/YorNoise_preparation_scripts/YorNoiseUrbanSound8KwithAdditionalColumnsForMCLNN.csv)  file.
4. Generate the indices for the folds using the [Index Generator](https://github.com/fadymedhat/MCLNN/tree/master/index_generator) script.
