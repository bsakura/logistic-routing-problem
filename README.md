# Logistic Routing Problem

<img src="https://picjumbo.com/wp-content/uploads/white-tir-truck-in-motion-driving-on-highway_free_stock_photos_picjumbo_DSC04205-1080x720.jpg" class="img-responsive" width="50%" height="50%"><img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Luftaufnahmen_Nordseekueste_2013_05_by-RaBoe_tele_46.jpg" class="img-responsive" width="50%" height="50%">

## Tujuan Tugas
1. Review materi pathfinding pada mata kuliah Strategi Algoritma.
2. Mengenal multiple-agent TSP.
3. Melakukan visualisasi data.

## Deskripsi Masalah
Welcome to **Oldenburg** ! Kota kecil cantik ini merupakan sebuah kota kecil di barat lau kota Bremen , Jerman , dengan penduduk kurang lebih 168 ribu jiwa [2018]. Kota kecil ini cocok menjadi lahan uji coba untuk melakukan pemodelan sederhana pembuatan rute pengantaran logistik.<br>
Setiap beberapa jam sekali, sebuah perusahaan logistik akan mengirimkan beberapa kurirnya untuk mengantar barang dari kantor pusat mereka ke beberapa titik tujuan yang tersebar di penjuru kota Oldenburg. Anda diminta untuk mencari rute untuk seluruh kurir sehingga jarak yang ditempuh oleh semua kurir paling kecil, sehingga perusahaan logistik dapat menghemat biaya bensin.

## Multiple-Agent TSP

The Multiple Traveling Salesman Problem (mTSP) is a generalization of the Traveling Salesman Problem (TSP) in which more than one salesman is allowed. Given a set of cities, one depot (where m salesmen are located), and a cost metric, the objective of the mTSP is to determine a set of routes for m salesmen so as to minimize the total cost of the m routes

## Algorithm Approach

### Ant Colony Optimization
To apply ACO to the TSP, we consider the graph defined by associating the set of cities with the set of vertices of the graph. This graph is called construction graph. Since in the TSP it is possible to move from any given city to any other city, the construction graph is fully connected and the number of vertices is equal to the number of cities. We set the lengths of the edges between the vertices to be proportional to the distances between the cities represented by these vertices and we associate pheromone values and heuristic values with the edges of the graph. Pheromone values are modified at runtime and represent the cumulated experience of the ant colony, while heuristic values are problem dependent values that, in the case of the TSP, are set to be the inverse of the lengths of the edges.<br>

The ants construct the solutions as follows. Each ant starts from a randomly selected city (vertex of the construction graph). Then, at each construction step it moves along the edges of the graph. Each ant keeps a memory of its path, and in subsequent steps it chooses among the edges that do not lead to vertices that it has already visited. An ant has constructed a solution once it has visited all the vertices of the graph. At each construction step, an ant probabilistically chooses the edge to follow among those that lead to yet unvisited vertices. The probabilistic rule is biased by pheromone values and heuristic information: the higher the pheromone and the heuristic value associated to an edge, the higher the probability an ant will choose that particular edge. Once all the ants have completed their tour, the pheromone on the edges is updated. Each of the pheromone values is initially decreased by a certain percentage. Each edge then receives an amount of additional pheromone proportional to the quality of the solutions to which it belongs (there is one solution per ant).<br>

This procedure is repeatedly applied until a termination criterion is satisfied.
<br>

### A* Star Algorithm
The A* (or A star) algorithm is a search algorithm which finds the shortest path between two nodes. It is considered as an extension of the Dijkstra algorithm, but tries to improve the runtime by using a heuristic to find the optimal solution. An example for such an heuristic would be the air-line distance (euclidean distance) between the start- and endpoint.<br>
Normally the A* algorithm is used to find the shortest path from node a to node b in a graph, but it is can be modifed to solve the TSP problem.<br>
1. Add the start node s to the OPEN list.
2. If the OPEN list is empty, end the algorithm with no result. In this case a solution can not found.
3. Chose node n from the OPEN list which has the minimal {\displaystyle f'(i)} and move it from the OPEN to the CLOSED list.
4. If node n is the destination node the algorithm has found the optimal solution and terminates. To get the shortest path from the start node to the end node travel back from n to s.
5. Otherwise expand n.

## Use The Program

In using the program there are several requirements that are ought to be installed in your computer beforehand to ensure that the program runs okay.

### Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install:

1. [networkx](https://networkx.github.io/documentation/stable/install.html)

```bash
pip install networkx
```
2. [matplotlib](https://pypi.org/project/matplotlib/)

```bash
pip install matplotlib
```
3. [more-itertools](https://pypi.org/project/more-itertools/)

```bash
pip install more-itertools
```
4. [numpy](https://pypi.org/project/numpy/)

```bash
pip install numpy
```


### Run
1. Clone this repository or simply download the zip
2. In your project directory of this cloned repository, open the folder src and run your cmd

```bash
python main.py
```
3. Several inputs are going to be requested in your console, fill the node file with the name of the node and edge files desired in txt, be sure to add the files in the data folder.

```bash
Samlekum, welcome to mini mtsp
Enter the node file in txt: OLnode.txt
Enter the edge file in txt: OLedge.txt
```
4. Fill the next field with the number of destinations you want to have excluding the starting point, and fill the field with the requested parameters.

```bash
Number of destination excluding starting point: 3
Starting point: 3
Destination -1: 4
Destination -2: 5
Destination -3: 6
How many salesperson(s) we got: 2
```
5. The program will show you the matrix representation of each salesperson's destinations, the route it takes them to complete their tour, and the visualization of their routes in different colors.

#### Milestone 1
Graph and subgraph of Oldenburg and SanFransisco had been initiated and created using networkx with the destinations as the nodes and the roads connecting them as the edges. The destinations in question are obtained by the user's input by cmd. The distances between the destinations had been implemented into matrix of distances for each salesperson(s).

#### Milestone 2
The routes taken by each salespersons had been built and shown for each one of them using a-star algorithm and optimized by the ant colony algorithm.

#### Milestone 3
Visualization had been presented for all nodes and edges in the graph and the routes for each salesperson had been marked in different colors and sizes of the nodes and edges.

## References
[1] Dataset : https://www.cs.utah.edu/~lifeifei/SpatialDataset.htm<br>
[2] mTSP introduction : https://neos-guide.org/content/multiple-traveling-salesman-problem-mtsp<br>
[3] ACO optimization : https://github.com/Akavall/AntColonyOptimization<br>
[4] Networkx for Python : https://networkx.github.io/<br>
[5]  Li, Feifei, Dihan Cheng, Marios Hadjieleftheriou, George Kollios, and Shang-Hua Teng. "On trip planning queries in spatial databases." In International symposium on spatial and temporal databases, pp. 273-290. Springer, Berlin, Heidelberg, 2005.

## Credits
Thank you for Li Fei Fei et. al. for providing the data.

## Final Words
Akhir Kata, selamat bersenang-senang ! It's not worth it if you're not having fun. :)

### Author
Byan Sakura
13518066