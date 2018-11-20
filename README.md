# NN_quantization
int8 quantization of NN for FPGA implementation (tensorflow version)

> The basic idea of the NN_quantization involves in construct a CAFFE network from its corresponding tensorflow version and then change the parameters from float32 to int8 or int16.

### int8 quantization

  #### basic idea: 
  
  *reduce parameter bits and properly sacrifice accuracy*

For example, we get a float32 number ∆ and we want the int8 representation of ∆. 

* tmp = ∆ * 2<sup>k</sup>, make tmp in the range 64 ~ 128, ∆ * 2<sup>k</sup> means ∆ moves left k. k = math.floor(math.log(128/∆, 2))
* tmp is still a float and we should change it to be an int. tmp = round(tmp), new∆ = tmp / 2<sup>k</sup> meaning tmp move left key to get the new float32 representation of ∆.
* we should save k and new∆. Most importantly new∆ should be resaved to tensorflow model.