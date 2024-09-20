# Earth-like Characterization Yield Random Forest Model

Context, description of the dataset, and analysis are described in the paper [Morgan et al. 2024](LINK HERE)

To use the Random Forest model presented in the paper, Python is necessary as well as the following packages:

`pip install numpy pandas scikit-learn xlrd`

## Usage

Once the packages are installed, open a Python instance (it can be a script, a Jupiter Notebook, ipython etc.) and use the following commands to load the Random Forest:

`from morgan2024 import *`

`rf = RF_Morgan2024('BAND')`

These lines will work if the dataset file "Morgan2024_dataset.xls" is in the same folder as the python file "morgan2024.py". The 'BAND' parameter in the second line must be substituted with one of the following: 'VIS', 'NUV', or 'NIR'.

Once the Random Forest has been loaded, it will be possible to use it to simulate Earth-like characterization yield by using the following command:

`rf.sim(diameter, loc(contrast), throughput, iwa)`

Substitute the 'diameter' with the telescope diameter value, the 'log(contrast)' with the loarithm of the contrast ratio, the 'throughput' with the telescope throughput value, and 'iwa' with the inner working angle (IWA) value.

## Example

`In[1]: from morgan2024 import *`

`In[2]: rf = RF_Morgan2024('VIS')`

`In[3]: rf.sim(6, -10, 0.1, 20)`

`Out[4]: 13.29610730168751`

## Authors
* Rhonda Morgan (Jet Propulsion Laboratory, California Institute of Technology)
* Michael Turmon (Jet Propulsion Laboratory, California Institute of Technology)
* Dmitry Savransky (Cornell University)
* Mario Damiano (Jet Propulsion Laboratory, California Institute of Technology)
* Renyu Hu (Jet Propulsion Laboratory, California Institute of Technology)
* Bertrand Mennesson (Jet Propulsion Laboratory, California Institute of Technology)
* Eric E. Mamajek (Jet Propulsion Laboratory, California Institute of Technology)
* Tyler D. Robinson (University of Arizona)
* Armen Tokadjian (Jet Propulsion Laboratory, California Institute of Technology)

## References

Morgan et al. 2024, [HWO Yield Sensitivities in the NIR and NUV](LINK HERE).

## Acknowledgement
Part of this research was carried out at the Jet Propulsion Laboratory, California Institute of Technology, under a contract with the National Aeronautics and Space Administration (80NM0018D0004).

## License
Copyright © 2024, by the California Institute of Technology. ALL RIGHTS RESERVED. United States Government Sponsorship acknowledged. Any commercial use must be negotiated with the Office of Technology Transfer at the California Institute of Technology.

This software may be subject to U.S. export control laws. By accepting this software, the user agrees to comply with all applicable U.S. export laws and regulations. User has the responsibility to obtain export licenses, or other export authority as may be required before exporting such information to foreign countries or providing access to foreign persons.

Licensed under the Apache License, Version 2.0 (the "Licence"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## BUGS!!!
For any issues and bugs please send an e-mail at [mario.damiano@jpl.nasa.gov](mario.damiano@jpl.nasa.gov).
