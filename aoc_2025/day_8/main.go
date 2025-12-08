package main

import (
	"container/heap"
	"fmt"
	"log"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

type Box struct {
	x, y, z int
}

func calculateEuclideanDistance(a, b Box) float64 {
	d1 := float64(a.x - b.x)
	d2 := float64(a.y - b.y)
	d3 := float64(a.z - b.z)
	return math.Sqrt(d1*d1 + d2*d2 + d3*d3)
}

type Distance struct {
	d    float64
	i, j int
}

type DistanceHeap []Distance

func (h DistanceHeap) Len() int           { return len(h) }
func (h DistanceHeap) Less(i, j int) bool { return h[i].d < h[j].d }
func (h DistanceHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *DistanceHeap) Push(x any) {
	*h = append(*h, x.(Distance))
}

func (h *DistanceHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type UnionFind struct {
	parent []int
	size   []int
}

func (uf *UnionFind) Find(x int) int {
	if uf.parent[x] != x {
		uf.parent[x] = uf.Find(uf.parent[x])
	}

	return uf.parent[x]
}

func (uf *UnionFind) Union(a, b int) int {
	rootA := uf.Find(a)
	rootB := uf.Find(b)

	if rootA == rootB {
		return uf.size[rootA]
	}

	if uf.size[rootA] < uf.size[rootB] {
		rootA, rootB = rootB, rootA
	}

	uf.parent[rootB] = rootA
	uf.size[rootA] += uf.size[rootB]
	return uf.size[rootA]
}

func NewUnionFind(n int) *UnionFind {
	parent := make([]int, n)
	size := make([]int, n)

	for i := 0; i < n; i++ {
		parent[i] = i
		size[i] = 1
	}

	return &UnionFind{
		parent: parent,
		size:   size,
	}
}

func main() {
	data, err := os.ReadFile("day_8/data.txt")
	if err != nil {
		log.Fatalln(err)
	}

	lines := strings.Split(string(data), "\n")
	boxes := make([]Box, 0, len(lines))
	for _, line := range lines {
		coords := strings.Split(line, ",")

		x, err := strconv.Atoi(coords[0])
		if err != nil {
			log.Fatalln(err)
		}

		y, err := strconv.Atoi(coords[1])
		if err != nil {
			log.Fatalln(err)
		}

		z, err := strconv.Atoi(coords[2])
		if err != nil {
			log.Fatalln(err)
		}
		boxes = append(boxes, Box{x: x, y: y, z: z})
	}

	distanceHeap := &DistanceHeap{}
	heap.Init(distanceHeap)
	for i := 0; i < len(boxes); i++ {
		for j := i + 1; j < len(boxes); j++ {
			d := calculateEuclideanDistance(boxes[i], boxes[j])
			heap.Push(distanceHeap, Distance{d: d, i: i, j: j})
		}
	}

	connectionsCount := 0
	uf := NewUnionFind(len(boxes))
	for distanceHeap.Len() > 0 {
		distance := heap.Pop(distanceHeap).(Distance)

		i := distance.i
		j := distance.j

		sizeAfterUnion := uf.Union(i, j)
		if sizeAfterUnion == len(boxes) {
			fmt.Println("Part 2: ", boxes[i].x*boxes[j].x)
			break
		}

		connectionsCount++
		if connectionsCount == 1000 {
			circuitSizes := append([]int{}, uf.size...)
			slices.SortFunc(circuitSizes, func(a, b int) int {
				return b - a
			})
			fmt.Println("Part 1: ", circuitSizes[0]*circuitSizes[1]*circuitSizes[2])
		}
	}
}
