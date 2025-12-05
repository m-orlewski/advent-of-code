package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("day_5/data.txt")
	if err != nil {
		log.Fatalln(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var freshIds [][2]int
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			break
		}

		ids := strings.Split(line, "-")

		l, err := strconv.Atoi(ids[0])
		if err != nil {
			log.Fatalln(err)
		}

		r, err := strconv.Atoi(ids[1])
		if err != nil {
			log.Fatalln(err)
		}

		freshIds = append(freshIds, [2]int{l, r})
	}

	var spoiledIds []int
	for scanner.Scan() {
		line := scanner.Text()
		id, err := strconv.Atoi(line)
		if err != nil {
			log.Fatalln(err)
		}

		spoiledIds = append(spoiledIds, id)
	}

	var count1 int
	for _, spoiledId := range spoiledIds {
		var found bool
		for _, freshId := range freshIds {
			if spoiledId >= freshId[0] && spoiledId <= freshId[1] {
				found = true
				break
			}
		}

		if found {
			count1++
		}
	}

	fmt.Println(count1)

	slices.SortFunc(freshIds, func(a, b [2]int) int {
		d := a[0] - b[0]
		if d != 0 {
			return d
		}

		return a[1] - b[1]
	})

	var mergedRanges [][2]int
	for _, ids := range freshIds {
		start, end := ids[0], ids[1]
		if mergedRanges == nil || start > mergedRanges[len(mergedRanges)-1][1]+1 {
			mergedRanges = append(mergedRanges, [2]int{start, end})
		} else {
			mergedRanges[len(mergedRanges)-1][1] = max(end, mergedRanges[len(mergedRanges)-1][1])
		}
	}

	var count2 int
	for _, mergedRange := range mergedRanges {
		count2 += mergedRange[1] - mergedRange[0] + 1
	}

	fmt.Println(count2)
}
