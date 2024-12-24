This script generates microstructure-esque structures by growing randomly placed points (or seeds). These continue expanding until another 'grain' or 'plate' is found.

Each grain is given:
1. A random location within the grid 
2. A random growth factor that controls how likely the grain is to grow each iteration.

grain growth wraps around the edge of the map

Example of what this can achieve are shown below:

![image](https://github.com/user-attachments/assets/ead15901-cb41-40e3-8c03-4f263def7bc0)
Figure 1: 6 Initial grains in a 140x140 grid

![image](https://github.com/user-attachments/assets/16c5fee9-8822-4673-ade6-76aa253e9f35)
Figure 2: 25 Initial grains in a 700x700 grid

![image](https://github.com/user-attachments/assets/223d8686-000a-43eb-abf1-ff22403412be)
Figure 3: 250 Grains in a 700x700 grid
