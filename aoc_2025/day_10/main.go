package main

import (
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

type State []bool
type Action []int

func (s State) ApplyAction(a Action) State {
	newState := append(State{}, s...)
	for _, i := range a {
		newState[i] = !s[i]
	}

	return newState
}

func encodeState(s State) uint32 {
	var x uint32
	for i, v := range s {
		if v {
			x |= 1 << uint(i)
		}
	}
	return x
}

func GetTargetStateAndActions(fields []string) (State, []Action) {
	targetState := State{}
	for _, s := range fields[0][1 : len(fields[0])-1] {
		if s == '.' {
			targetState = append(targetState, false)
		} else {
			targetState = append(targetState, true)
		}
	}

	actions := make([]Action, 0, len(fields)-2)
	for _, field := range fields[1 : len(fields)-1] {
		field := field[1 : len(field)-1]
		buttons := strings.Split(field, ",")

		action := make([]int, 0, len(buttons))
		for _, button := range buttons {
			b, err := strconv.Atoi(button)
			if err != nil {
				log.Fatalln(err)
			}
			action = append(action, b)
		}

		actions = append(actions, action)
	}

	return targetState, actions
}

func BFS(initial, target State, actions []Action) int {
	type Node struct {
		State State
		Depth int
	}

	q := []Node{{State: initial, Depth: 0}}
	visited := map[uint32]bool{encodeState(initial): true}

	for len(q) > 0 {
		cur := q[0]
		q = q[1:]

		if slices.Equal(cur.State, target) {
			return cur.Depth
		}

		for _, a := range actions {
			next := cur.State.ApplyAction(a)
			if !visited[encodeState(next)] {
				visited[encodeState(next)] = true
				q = append(q, Node{State: next, Depth: cur.Depth + 1})
			}
		}
	}

	return -1
}

func main() {
	data, err := os.ReadFile("day_10/data.txt")
	if err != nil {
		log.Fatalln(err)
	}

	lines := strings.Split(string(data), "\n")

	var answer1 int
	for _, line := range lines {
		fields := strings.Split(line, " ")
		target, actions := GetTargetStateAndActions(fields)
		start := make(State, len(target))
		answer1 += BFS(start, target, actions)
	}

	fmt.Println("Part 1: ", answer1)
}
