package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func panicIfErr(err error) {
	if err != nil {
		panic(err)
	}
}

func main() {
	data, err := os.ReadFile("day_3/data.txt")
	panicIfErr(err)

	banks := strings.Split(string(data), "\n")

	outputJoltage1 := 0
	for _, bank := range banks {
		// find first digit
		firstDigit := 0
		firstDigitIdx := -1
		for i := 9; i >= 1; i-- {
			firstDigitIdx = strings.Index(bank[:len(bank)-1], strconv.Itoa(i))
			if firstDigitIdx != -1 {
				firstDigit = i
				break
			}
		}

		// find second digit
		secondDigit := 0
		for i := 9; i >= 1; i-- {
			idx := strings.Index(bank[firstDigitIdx+1:], strconv.Itoa(i))
			if idx != -1 {
				secondDigit = i
				break
			}
		}

		outputJoltage1 += 10*firstDigit + secondDigit
	}

	fmt.Println("1) Total output joltage = ", outputJoltage1)

	outputJoltage2 := 0
	for _, bank := range banks {
		prevIdx := -1
		digits := [12]int{}
		for i := 0; i < len(digits); i++ {
			for j := 9; j >= 1; j-- {
				idx := strings.Index(bank[prevIdx+1:len(bank)-len(digits)+i+1], strconv.Itoa(j))
				if idx != -1 {
					prevIdx = idx + prevIdx + 1 // idx refers the substr, prevIdx must refer to the entire string
					digits[i] = j
					break
				}
			}
		}

		for i, digit := range digits {
			outputJoltage2 += int(math.Pow10(12-i-1)) * digit
		}
	}

	fmt.Println("2) Total output joltage = ", outputJoltage2)
}
