package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
	"slices"
)

func countTimelines(manifold [][]byte, col, row int, memo map[[2]int]int) int {
	if row == len(manifold)-1 {
		return 1 // this timeline is over
	}

	k := [2]int{row, col}
	if v, ok := memo[k]; ok {
		return v
	}

	var c int
	if manifold[row][col] == '^' {
		// timeline splits
		if col-1 >= 0 {
			c += countTimelines(manifold, col-1, row, memo)
		}

		if col+1 < len(manifold[row]) {
			c += countTimelines(manifold, col+1, row, memo)
		}
	} else {
		// timeline continues
		c = countTimelines(manifold, col, row+1, memo)
	}

	memo[k] = c
	return c
}

func main() {
	data, err := os.ReadFile("day_7/data.txt")
	if err != nil {
		log.Fatalln(err)
	}

	var splitCount int
	manifold := bytes.Split(data, []byte("\n"))
	for i := 1; i < len(manifold); i++ {
		for j := range manifold[i] {
			if manifold[i-1][j] != 'S' && manifold[i-1][j] != '|' {
				continue
			}

			if manifold[i][j] == '^' {
				// split the beacon
				manifold[i][j-1] = '|'
				manifold[i][j+1] = '|'
				splitCount++
			} else {
				manifold[i][j] = '|'
			}
		}
	}

	fmt.Println("Total number of beam splits: ", splitCount)

	manifold = bytes.Split(data, []byte("\n"))
	timelineCount := countTimelines(manifold, slices.Index(manifold[0], 'S'), 1, map[[2]int]int{})
	fmt.Println("Total number of timelines: ", timelineCount)
}
