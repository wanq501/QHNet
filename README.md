<h1> 
  <p align=center> QHNet: A Novel Quad-Head Network for Real-Time Detection of Intruding Drones </p>
<div align="center">

![Python 3.9](https://img.shields.io/badge/python-3.9-g)
![pytorch 1.12.1](https://img.shields.io/badge/pytorch-1.12.1-blue.svg)
[![docs](https://img.shields.io/badge/docs-latest-blue)](README.md)

</div>
</h1>
<img src="ultralytics/assets/Fig0.png" width="1500">

## Model Zoo 

<table>
  <thead align="center">
    <tr>
      <th>Model</th>
      <th>Resolution</th>
      <th>Epoch</th>
      <th>Params(M)</th>
      <th>FLOPs(G)</th>
      <th>$AP$</th>
      <th>$AP_{50}$</th>
      <th>$AP_{75}$</th>
      <th>BaiduYun Download</th>
      <th>Google Download</th>
    </tr>
  </thead>
  <tbody align="center">
    <tr>
      <td>QHNet-N</td>
      <td>640</td>
      <td>200</td>
      <td>2.8</td>
      <td>12.0</td>
      <td>57.1</td>
      <td>88.9</td>
      <td>65.9</td>
      <td><a href="https://pan.baidu.com/s/1hySq6bXcZP12WTg-ukFnOA?pwd=e8fm">weight</a></td>
      <td>---</td>
    </tr>
    <tr>
      <td>QHNet-S</td>
      <td>640</td>
      <td>200</td>
      <td>10.4</td>
      <td>35.1</td>
      <td>60.2</td>
      <td>91.2</td>
      <td>70.1</td>
      <td><a href="https://pan.baidu.com/s/1ka7D4E71CMXBwDhz3gpXOw?pwd=f3ak">weight</a></td>
      <td>---</td>
    </tr>
    <tr>
      <td>QHNet-M</td>
      <td>640</td>
      <td>200</td>
      <td>17.9</td>
      <td>71.1</td>
      <td>62.1</td>
      <td>92.8</td>
      <td>71.4</td>
      <td><a href="https://pan.baidu.com/s/1TC71JOBn_mgWrmv6ZhSQ2w?pwd=k5jq">weight</a></td>
      <td>---</td>
    </tr>
    <tr>
      <td>QHNet-L</td>
      <td>640</td>
      <td>200</td>
      <td>24.0</td>
      <td>120.4</td>
      <td>63.1</td>
      <td>93.2</td>
      <td>71.9</td>
      <td><a href="https://pan.baidu.com/s/1pITBN9lTtWW9Zx6jA5xUdA?pwd=aurc">weight</a></td>
      <td>---</td>
    </tr>
    <tr>
      <td>QHNet-X</td>
      <td>640</td>
      <td>200</td>
      <td>37.1</td>
      <td>183.8</td>
      <td>64.0</td>
      <td>93.8</td>
      <td>74.3</td>
      <td><a href="https://pan.baidu.com/s/1ml-ihrPirE24wTlU77rliw?pwd=qukr">weight</a></td>
      <td>---</td>
    </tr>
  </tbody>
</table>

- Results of the mAP are evaluated on [DUT-Anti-UAV](https://github.com/wangdongdut/DUT-Anti-UAV) dataset with the input
  resolution of 640×640.



## Dependencies and Installation 

1. Clone and enter the repo.

   ```shell
   git clone https://github.com/wanq501/QHNet.git
   cd QHNet
   ```

2. Run `install.sh`.

   ```shell
   pip install -e .
   ```

## Training and Evaluation 

1. Training


   ```shell
   python tools/train.py
   ```


2. Evaluation

   ```shell
   python tools/val.py
   ```



3. Test

   ```shell
   python tools/test.py
   ```

4. Detect

   ```shell
   python tools/detect.py
   ```

- Note: Each script includes detailed instructions on how to set parameters and use the script properly.

## Citation

If you find our repo useful for your research, please cite us:

```

```

## License

Licensed under a [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/) for Non-commercial use only. Any commercial use should get formal permission first.



