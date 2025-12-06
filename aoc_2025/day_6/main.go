package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Operation struct {
	operator string
	operands []string
}

func loadData1() []Operation {
	file, err := os.Open("day_6/data.txt")
	if err != nil {
		log.Fatalln(err)
	}
	defer file.Close()

	fields := [][]string{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		fields = append(fields, strings.Fields(line))
	}

	operations := []Operation{}

	for j := 0; j < len(fields[0]); j++ {
		operands := []string{}
		longest := 0
		for i := 0; i < len(fields)-1; i++ {
			longest = max(longest, len(fields[i][j]))
			operands = append(operands, fields[i][j])
		}

		// pad with zeros
		for i := range operands {
			operands[i] = strings.Repeat("0", longest-len(operands[i])) + operands[i]
		}
		operations = append(operations, Operation{operator: fields[len(fields)-1][j], operands: operands})
	}

	return operations
}

func loadData2() []Operation {
	data, err := os.ReadFile("day_6/data.txt")
	if err != nil {
		log.Fatalln(err)
	}

	lines := strings.Split(string(data), "\n")
	operators := strings.Fields(lines[len(lines)-1])
	lines = lines[:len(lines)-1]

	operations := []Operation{}
	var operands []string
	for j := 0; j < len(lines[0]); j++ {
		var operand string
		for i := 0; i < len(lines); i++ {
			if lines[i][j] == ' ' {
				continue
			}
			operand += string(lines[i][j])
		}

		if operand != "" {
			operands = append(operands, operand)
		} else if operand == "" {
			operations = append(operations, Operation{operator: operators[len(operations)], operands: append([]string{}, operands...)})
			operands = []string{}
		}
	}

	operations = append(operations, Operation{operator: operators[len(operations)], operands: append([]string{}, operands...)})

	return operations
}

func calculateTotal(operations []Operation) (total int) {
	for _, operation := range operations {
		var subtotal int
		if operation.operator == "*" {
			subtotal = 1
		}

		for _, operand := range operation.operands {
			o, err := strconv.Atoi(operand)
			if err != nil {
				log.Fatalln(err)
			}
			if operation.operator == "*" {
				subtotal *= o
			} else {
				subtotal += o
			}
		}

		total += subtotal
	}

	return total
}

func main() {
	fmt.Println(calculateTotal(loadData1()))
	fmt.Println(calculateTotal(loadData2()))
}
