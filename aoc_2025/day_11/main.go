package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

func Solve(adjList map[string][]string, start, end string) int {
	type key struct {
		node string
		dac  bool
		fft  bool
	}
	memo := map[key]int{}

	visited := map[string]bool{}

	var dfs func(string, bool, bool) int

	dfs = func(cur string, dac, fft bool) int {
		if cur == "dac" {
			dac = true
		}
		if cur == "fft" {
			fft = true
		}

		k := key{cur, dac, fft}
		if v, ok := memo[k]; ok {
			return v
		}

		if cur == end {
			if dac && fft {
				return 1
			}
			return 0
		}

		visited[cur] = true
		var total int
		for _, neighbor := range adjList[cur] {
			if !visited[neighbor] {
				total += dfs(neighbor, dac, fft)
			}
		}

		memo[k] = total
		delete(visited, cur)
		return total
	}

	if start == "you" {
		return dfs(start, true, true)
	} else {
		return dfs(start, false, false)
	}

}

func main() {
	data, err := os.ReadFile("day_11/data.txt")
	if err != nil {
		log.Fatalln(err)
	}

	lines := strings.Split(string(data), "\n")
	adjList := map[string][]string{}
	for _, line := range lines {
		line = strings.Replace(line, ":", "", 1)
		fields := strings.Split(line, " ")
		adjList[fields[0]] = fields[1:]
	}

	fmt.Println("Part 1: ", Solve(adjList, "you", "out"))
	fmt.Println("Part 2: ", Solve(adjList, "svr", "out"))
}
