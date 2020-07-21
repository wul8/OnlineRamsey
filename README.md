# Online Ramsey Game Simulation</br>
## Background</br>
This project is designed to help solve the problem based on Online Ramsey Game introduced by Beck[1] and Friedguet et al.[2]. The two-colors online ramsey game is described as following: </br></br>
The online ramsey game is a combinational game between two players, Builder and Painter. Starting from infinite set of vertices, Builder connects two vertices with an edge and Painter immediately paint it with color Red or color Blue. The goal of builder is to force painter to create a speicific monochornomatic subgraph **H**, for example, path with 4 vertices(**P4**), circle with 5 vertices(**C5**), complete graph with 4 vertices(**K4**). The goal of Painter is trying to avoid creating such monochromatic subgraph **H**.</br></br>
The oneline ramsey problem is to find the minimum number of rounds **R2(H)** required for Builder's winning strategy and maximum number of rounds **R2'(H)** for Painter's winning strategy, aka two color online ramsey number. In the past few years, there're some incredible progresses going on with two-colors oneline ramsey theory. For example, Grytczuk et al.[3] has proven that R2(Pn) <= 4n -7 and R2(Pn)>=2n-3. Pralat[4] has implemented and ran programs written in C/C++ that can simulate two color online game of paths</br></br>
## What's in it
1. This program, in a step way further, extends simulation of two colors online ramsey game to multicolor online ramsey game in Python using backtracking with alpha beta prunning algorithm. It outputs corresponding online ramsey number.</br>
2. This program supports simulation with different initial configuration. For example, the program can stimulate R3(P5) (3 color Online Rmasey number of a monochromatic path with 4 verteces) with initial graph P3 (monochronmatic path with 3 vertices)</b4>
3. Convinient User Interface for people who might not be familir with python. 
## How to run
1. Part of the scripts have been converted to executable application. Click on start.exe to run. More features will be added on User Interface.
## Dependencies
networkx 3.7 / matplotlib 3.2.1/ pickle 3.8.4 
