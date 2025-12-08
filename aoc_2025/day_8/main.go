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

	nextId := 1
	connectionsCount := 0
	// maps circuitId -> indices of boxes in it
	circuits := map[int][]int{}
	// maps circuitId -> count of boxes in it
	circuitCounts := map[int]int{}
	// maps box index -> circuit id it's in
	boxCircuits := map[int]int{}
	for distanceHeap.Len() > 0 {
		distance := heap.Pop(distanceHeap).(Distance)

		i := distance.i
		j := distance.j

		c1, ok1 := boxCircuits[i]
		c2, ok2 := boxCircuits[j]

		// 2) neither box is in a circuit
		if !ok1 && !ok2 {
			circuits[nextId] = append(circuits[nextId], i, j)
			circuitCounts[nextId] = len(circuits[nextId])
			boxCircuits[i] = nextId
			boxCircuits[j] = nextId
			nextId++
		} else if !ok1 {
			circuits[c2] = append(circuits[c2], i)
			circuitCounts[c2] = len(circuits[c2])
			boxCircuits[i] = c2
		} else if !ok2 {
			circuits[c1] = append(circuits[c1], j)
			circuitCounts[c1] = len(circuits[c1])
			boxCircuits[j] = c1
		} else if ok1 && ok2 {
			// merge 2 circuits
			if c1 != c2 {
				circuits[c1] = append(circuits[c1], circuits[c2]...)
				circuitCounts[c1] = len(circuits[c1])
				for _, boxId := range circuits[c2] {
					boxCircuits[boxId] = c1
				}
				delete(circuits, c2)
				delete(circuitCounts, c2)
			}
		}

		connectionsCount++
		if connectionsCount == 1000 {
			break
		}
	}

	counts := []int{}
	for _, v := range circuitCounts {
		counts = append(counts, v)
	}
	slices.SortFunc(counts, func(x, y int) int {
		return y - x
	})

	fmt.Println("Part 1: ", counts[0]*counts[1]*counts[2])
}
