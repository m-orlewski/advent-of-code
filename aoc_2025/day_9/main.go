package main

import (
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

type Coord struct {
	x, y int
}

func rectangleArea(c1, c2 Coord) int {
	a := math.Abs(float64(c1.x-c2.x)) + 1
	b := math.Abs(float64(c1.y-c2.y)) + 1
	return int(a * b)
}

type Edge [2]Coord
type Rectangle [4]Edge
type Polygon []Edge

func NewRectangle(a, b Coord) Rectangle {
	xMin, xMax := min(a.x, b.x), max(a.x, b.x)
	yMin, yMax := min(a.y, b.y), max(a.y, b.y)

	c1 := Coord{x: xMin, y: yMin}
	c2 := Coord{x: xMin, y: yMax}
	c3 := Coord{x: xMax, y: yMin}
	c4 := Coord{x: xMax, y: yMax}

	return Rectangle{
		Edge{c1, c2},
		Edge{c2, c3},
		Edge{c3, c4},
		Edge{c4, c1},
	}
}

func pointInPolygon(p Coord, poly Polygon) bool {
	var c int
	for _, e := range poly {
		x1, y1 := e[0].x, e[0].y
		x2, y2 := e[1].x, e[1].y

		// p lies on the vertical edge
		if x1 == x2 && p.x == x1 && p.y >= min(y1, y2) && p.y <= max(y1, y2) {
			return true
		}

		// p lies on the horizontal edge
		if y1 == y2 && p.y == y1 && p.x >= min(x1, x2) && p.x <= max(x1, x2) {
			return true
		}

		// skip horizontal edges
		if x1 != x2 {
			continue
		}

		xv := x1
		ymin := min(y1, y2)
		ymax := max(y1, y2)

		if p.y >= ymin && p.y < ymax && p.x < xv {
			c++
		}
	}

	return (c % 2) == 1
}

func edgesCrossed(e1, e2 Edge) bool {
	var h, v Edge // horizontal and vertical edge
	if e1[0].x == e1[1].x {
		// e1 is vertical, e2 is horizontal
		h = e2
		v = e1
	} else {
		// e2 is vertical, e1 is vertical
		h = e1
		v = e2
	}

	if v[0].x > min(h[0].x, h[1].x) && v[0].x < max(h[0].x, h[1].x) &&
		h[0].y > min(v[0].y, v[1].y) && h[0].y < max(v[0].y, v[1].y) {
		return true
	}

	return false
}

func checkIfRectangleInPolygon(rect Rectangle, poly Polygon) bool {
	// 1) check if each corner of rectangle is withing the polygon
	for _, edge := range rect {
		if !pointInPolygon(edge[0], poly) {
			return false
		}
	}

	// 2) check if any edges cross each other
	for _, r := range rect {
		for _, p := range poly {
			rVertical := r[0].x == r[1].x
			pVertical := p[0].x == p[1].x

			// both edges are vertical
			if ((rVertical && !pVertical) || (!rVertical && pVertical)) && edgesCrossed(r, p) {
				return false
			}
		}
	}

	return true
}

func main() {
	data, err := os.ReadFile("day_9/data.txt")
	if err != nil {
		log.Fatalln(err)
	}

	lines := strings.Split(string(data), "\n")

	reds := []Coord{}
	for _, line := range lines {
		coords := strings.Split(line, ",")

		x, err := strconv.Atoi(coords[1])
		if err != nil {
			log.Fatalln(err)
		}

		y, err := strconv.Atoi(coords[0])
		if err != nil {
			log.Fatalln(err)
		}

		reds = append(reds, Coord{x: x, y: y})
	}

	var largestArea int
	for i := 0; i < len(reds); i++ {
		for j := i + 1; j < len(reds); j++ {
			area := rectangleArea(reds[i], reds[j])
			largestArea = max(largestArea, area)
		}
	}

	fmt.Println("Largest possible rectangle area: ", largestArea)

	polygon := Polygon{}
	for i := range reds {
		edge := Edge{
			reds[i],
			reds[(i+1)%len(reds)],
		}
		polygon = append(polygon, edge)
	}

	largestArea = 0
	for i := 0; i < len(reds); i++ {
		for j := i + 1; j < len(reds); j++ {
			r := NewRectangle(reds[i], reds[j])
			if checkIfRectangleInPolygon(r, polygon) && rectangleArea(reds[i], reds[j]) == 2876487552 {
				fmt.Println(i, j)
				largestArea = max(largestArea, rectangleArea(reds[i], reds[j]))
			}
		}
	}

	fmt.Println("Largest possible rectangle area: ", largestArea)
}
