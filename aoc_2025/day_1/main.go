package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	data, err := os.ReadFile("day_1/data.txt")
	if err != nil {
		panic(err)
	}

	instructions := strings.Split(string(data), "\n")
	dial := 50
	password1 := 0
	password2 := 0
	for _, instruction := range instructions {
		direction := string(instruction[0])
		distance, err := strconv.Atoi(instruction[1:])
		if err != nil {
			panic(err)
		}

		fullCycles := int(math.Abs(float64(distance / 100)))
		distance %= 100

		if direction == "L" {
			distance = -distance
		}
		dial += distance

		password2 += fullCycles // each full cycle crosses zero

		// increment if remainder distance crossed zero (except when we started at zero)
		if (dial <= 0 && dial-distance != 0) || dial > 99 {
			password2++
		}

		dial = ((dial % 100) + 100) % 100 // to handle modulo of negative numbers (which is negative in Go)
		if dial == 0 {
			password1++
		}
	}

	// 6386
	fmt.Println("Passwords: ", password1, password2)
}
