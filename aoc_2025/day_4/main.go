package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func failIfErr(err error) {
	if err != nil {
		log.Fatalln(err)
	}
}

var neighbors = [...][2]int{
	{-1, -1}, {-1, 0}, {-1, 1},
	{0, -1}, {0, 1},
	{1, -1}, {1, 0}, {1, 1},
}

func countSurrounding(grid [][]byte, i, j int) (count int) {
	for _, neighbor := range neighbors {
		x, y := i+neighbor[0], j+neighbor[1]
		if x < 0 || x >= len(grid) || y < 0 || y >= len(grid[x]) {
			continue
		}

		if grid[x][y] == '@' {
			count++
		}
	}

	return count
}

func countAndRemove(grid [][]byte) int {
	toRemove := [][2]int{}
	for i, row := range grid {
		for j, col := range row {
			if col == '.' {
				continue
			}

			if countSurrounding(grid, i, j) < 4 {
				toRemove = append(toRemove, [2]int{i, j})
			}
		}
	}

	for _, ind := range toRemove {
		grid[ind[0]][ind[1]] = '.'
	}

	return len(toRemove)
}

func main() {
	data, err := os.ReadFile("day_4/data.txt")
	failIfErr(err)

	lines := strings.Split(string(data), "\n")
	grid := [][]byte{}
	for _, line := range lines {
		grid = append(grid, []byte(line))
	}

	// part 1
	count1 := countAndRemove(grid)

	// part 2
	count2 := count1
	for {
		c := countAndRemove(grid)
		if c == 0 {
			break
		}
		count2 += c
	}

	fmt.Println(count1)
	fmt.Println(count2)
}
