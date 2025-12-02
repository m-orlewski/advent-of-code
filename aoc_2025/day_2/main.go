package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func panicIfErr(err error) {
	if err != nil {
		panic(err)
	}
}

func isValidPart1(id int) bool {
	s := fmt.Sprintf("%d", id)

	if len(s)%2 == 0 && s[:len(s)/2] == s[len(s)/2:] {
		return false
	}

	return true
}

func isValidPart2(id int) bool {
	s := fmt.Sprintf("%d", id)

	for l := 1; l <= len(s)/2; l++ {
		if len(s)%l != 0 {
			continue
		}

		count := strings.Count(s, s[:l])
		if count == len(s)/l {
			return false
		}
	}

	return true
}

func main() {
	data, err := os.ReadFile("day_2/data.txt")
	panicIfErr(err)

	invalidIdsPart1 := 0
	invalidIdsPart2 := 0
	idRanges := strings.Split(string(data), ",")

	for _, idRange := range idRanges {
		start, end, _ := strings.Cut(idRange, "-")

		s, err := strconv.Atoi(start)
		panicIfErr(err)

		e, err := strconv.Atoi(end)
		panicIfErr(err)

		for id := s; id <= e; id++ {
			if !isValidPart1(id) {
				invalidIdsPart1 += id
			}

			if !isValidPart2(id) {
				invalidIdsPart2 += id
			}
		}
	}

	fmt.Println(invalidIdsPart1)
	fmt.Println(invalidIdsPart2)
}
