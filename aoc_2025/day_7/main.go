package main

import (
	"bytes"
	"fmt"
	"log"
	"os"
)

func main() {
	data, err := os.ReadFile("day_7/data.txt")
	if err != nil {
		log.Fatalln(err)
	}

	var splitCount1 int
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
				splitCount1++
			} else {
				manifold[i][j] = '|'
			}
		}
	}

	fmt.Println("Total number of beam splits: ", splitCount1)
}
