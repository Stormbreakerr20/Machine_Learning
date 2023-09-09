# Tensors: n-dimensional array EX numpy
# no.of axis = rank of tensor = no. of axis = no. of dimension != shape

# 0D Tensors: Scalers:  np.array(4)
# 1d - [1,2,3,4]:  np.array([1,2,3,4])
# Note: above is 1d tensor but 4d vector, Ex: [1,2] 1d-tensor but 2d-vector
# 2d - np.array([[1,2,3,4],[5,6,7,9]])  
# 3d - collection of 2d tensors : cube type which also has depth
# 4d - 1d collection of 3d tensors (basically cubes in array)
# 5d - matrix of 3d tensors (matrix of cubes i.e collection of 4d tensors)

# nd - collection of n-1d tensors


# Example of 3d tensors
# NLP: for string : i/p = Hi Luv, Hi yash

# represent as : Hi = [1,0,0] , Luv = [0,1,0], yash = [0,0,1]
# means sentence 1 = [[1,0,0],[0,1,0]], sentence 2 = [[1,0,0],[0,,1]]
# => i/p =[ [[1,0,0],[0,1,0]], [[1,0,0],[0,0,1]] ]  3d tensor  : shape = (2,2,3)

# Example of 4d tensors
# images: pixels collection : you take 2d matrix of R,G,B stack them and appear somewhat as cube : become 3d-tensors
# for 50 color images it become 4d-tensor: (50,3,1200,800)
# let pixel be of 1200*800 then above shape obtained

# 5d-tensors
# Videos: collection of images which are 4d tensors : they move so fast it is fastr than our perception of vision
#  let 4 video each 60 sec and 30fps : images = 1800 
# shape = (4,1800,3,1200,800)
