package main

import "testing"

// Assume your functions pointInPolygon, edgesCrossed, checkIfRectangleInPolygon are defined above.

func TestCheckIfRectangleInPolygon(t *testing.T) {
	tests := []struct {
		name string
		rect Rectangle
		poly Polygon
		want bool
	}{
		{
			name: "Rectangle fully inside polygon",
			rect: Rectangle{
				{{2, 2}, {2, 5}},
				{{2, 5}, {5, 5}},
				{{5, 5}, {5, 2}},
				{{5, 2}, {2, 2}},
			},
			poly: Polygon{
				{{0, 0}, {10, 0}},
				{{10, 0}, {10, 10}},
				{{10, 10}, {0, 10}},
				{{0, 10}, {0, 0}},
			},
			want: true,
		},
		{
			name: "Rectangle corner on polygon edge",
			rect: Rectangle{
				{{0, 0}, {0, 2}},
				{{0, 2}, {2, 2}},
				{{2, 2}, {2, 0}},
				{{2, 0}, {0, 0}},
			},
			poly: Polygon{
				{{0, 0}, {10, 0}},
				{{10, 0}, {10, 10}},
				{{10, 10}, {0, 10}},
				{{0, 10}, {0, 0}},
			},
			want: true,
		},
		{
			name: "Rectangle edge on polygon edge",
			rect: Rectangle{
				{{0, 2}, {0, 5}},
				{{0, 5}, {5, 5}},
				{{5, 5}, {5, 2}},
				{{5, 2}, {0, 2}},
			},
			poly: Polygon{
				{{0, 0}, {10, 0}},
				{{10, 0}, {10, 10}},
				{{10, 10}, {0, 10}},
				{{0, 10}, {0, 0}},
			},
			want: true,
		},
		{
			name: "Rectangle partially outside polygon",
			rect: Rectangle{
				{{8, 8}, {8, 12}},
				{{8, 12}, {12, 12}},
				{{12, 12}, {12, 8}},
				{{12, 8}, {8, 8}},
			},
			poly: Polygon{
				{{0, 0}, {10, 0}},
				{{10, 0}, {10, 10}},
				{{10, 10}, {0, 10}},
				{{0, 10}, {0, 0}},
			},
			want: false,
		},
		{
			name: "Rectangle corners inside but edges cross concave polygon",
			rect: Rectangle{
				{{3, 3}, {3, 7}},
				{{3, 7}, {7, 7}},
				{{7, 7}, {7, 3}},
				{{7, 3}, {3, 3}},
			},
			poly: Polygon{
				{{0, 0}, {10, 0}},
				{{10, 0}, {10, 2}},
				{{10, 2}, {2, 2}},
				{{2, 2}, {2, 8}},
				{{2, 8}, {10, 8}},
				{{10, 8}, {10, 10}},
				{{10, 10}, {0, 10}},
				{{0, 10}, {0, 0}},
			},
			want: false,
		},
		{
			name: "Rectangle fully outside polygon",
			rect: Rectangle{
				{{12, 12}, {12, 15}},
				{{12, 15}, {15, 15}},
				{{15, 15}, {15, 12}},
				{{15, 12}, {12, 12}},
			},
			poly: Polygon{
				{{0, 0}, {10, 0}},
				{{10, 0}, {10, 10}},
				{{10, 10}, {0, 10}},
				{{0, 10}, {0, 0}},
			},
			want: false,
		},
		{
			name: "Rectangle touching polygon vertex only",
			rect: Rectangle{
				{{10, 10}, {10, 12}},
				{{10, 12}, {12, 12}},
				{{12, 12}, {12, 10}},
				{{12, 10}, {10, 10}},
			},
			poly: Polygon{
				{{0, 0}, {10, 0}},
				{{10, 0}, {10, 10}},
				{{10, 10}, {0, 10}},
				{{0, 10}, {0, 0}},
			},
			want: false,
		},
		{
			name: "Rectangle exactly same as polygon",
			rect: Rectangle{
				{{0, 0}, {0, 10}},
				{{0, 10}, {10, 10}},
				{{10, 10}, {10, 0}},
				{{10, 0}, {0, 0}},
			},
			poly: Polygon{
				{{0, 0}, {0, 10}},
				{{0, 10}, {10, 10}},
				{{10, 10}, {10, 0}},
				{{10, 0}, {0, 0}},
			},
			want: true,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := checkIfRectangleInPolygon(tt.rect, tt.poly)
			if got != tt.want {
				t.Errorf("checkIfRectangleInPolygon() = %v, want %v", got, tt.want)
			}
		})
	}
}
