package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	data, err := os.ReadFile("day_12/data.txt")
	if err != nil {
		log.Fatalln(err)
	}

	presents := make([]int, 6)
	regions := []string{}
	fields := strings.Split(string(data), "\n\n")
	for id, field := range fields {
		if id == len(fields)-1 {
			regions = strings.Split(field, "\n")
		} else {
			presents[id] = strings.Count(field, "#")
		}
	}

	var answer int
	for _, region := range regions {
		fields := strings.Split(region, ": ")
		gridShapes := strings.Split(fields[0], "x")

		x, err := strconv.Atoi(gridShapes[0])
		if err != nil {
			log.Fatalln(err)
		}

		y, err := strconv.Atoi(gridShapes[1])
		if err != nil {
			log.Fatalln(err)
		}

		totalGridArea := x * y

		var totalShapeArea int
		for i, count := range strings.Split(fields[1], " ") {
			c, err := strconv.Atoi(count)
			if err != nil {
				log.Fatalln(err)
			}

			totalShapeArea += c * presents[i]
		}
		fmt.Println(totalGridArea, totalShapeArea)

		if float64(totalShapeArea)*1.2 <= float64(totalGridArea) {
			answer++
		}
	}

	fmt.Println(answer)
}
