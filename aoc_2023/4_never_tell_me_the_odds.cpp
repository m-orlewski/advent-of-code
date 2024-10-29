#include <iostream>
#include <vector>
#include <utility>
#include <fstream>
#include <sstream>

constexpr double LOWER_TEST_RANGE = 200000000000000;
constexpr double UPPER_TEST_RANGE = 400000000000000;

struct Position {
    double x, y, z;
};

struct Velocity {
    double x, y, z;
};

class Hailstone {
public:
    Hailstone(double px, double py, double pz, double vx, double vy, double vz): pos(Position{px, py, pz}), v(Velocity{vx, vy, vz}) {
        a = (double)vy/vx;
        b = py - a*px;
    }

    bool isIntersectionWithinTestRange(const Hailstone& other) const {
        // check if parallel
        if (a == other.a) {
            return false;
        }

        auto intersectionPoint = getIntersectionPoint(other);

        // check if it didn't happen in the future
        if (!isPointInFuture(intersectionPoint.first, intersectionPoint.second) ||
            !other.isPointInFuture(intersectionPoint.first, intersectionPoint.second)) {
                return false;
        }

        // check if within test range
        if (!isPointWithinTestRange(intersectionPoint.first, intersectionPoint.second)) {
            return false;
        }

        return true;
    }

private:
    Position pos;
    Velocity v;
    double a, b;

    std::pair<double, double> getIntersectionPoint(const Hailstone& other) const {
        double x = (other.b - b) / (a - other.a);
        double y = a*x + b;

        return {x, y};
    }

    bool isPointInFuture(double x, double y) const {
        if (v.x > 0 && x < pos.x) return false;
        if (v.x < 0 && x > pos.x) return false;
        if (v.y > 0 && y < pos.y) return false;
        if (v.y < 0 && y > pos.y) return false;

        return true;
    }

    bool isPointWithinTestRange(double x, double y) const {
        if (x < LOWER_TEST_RANGE || x > UPPER_TEST_RANGE) return false;
        if (y < LOWER_TEST_RANGE || y > UPPER_TEST_RANGE) return false;

        return true;
    }
};

int main(int argc, char* argv[]) {
    std::vector<Hailstone> hail;
    std::fstream file("data/input_4_never_tell_me_the_odds.txt", std::ios::in);

    std::string line;
    double px, py, pz, vx, vy, vz;
    char c;
    while (std::getline(file, line)) {
        std::istringstream ss(line);
        ss >> px >> c >> py >> c >> pz >> c >> vx >> c >> vy >> c >> vz;
        hail.emplace_back(px, py, pz, vx, vy, vz);
    }

    int numOfIntersections = 0;
    for (int i=0; i < hail.size(); i++) {
        for (int j=i+1; j < hail.size(); j++) {
             if (hail[i].isIntersectionWithinTestRange(hail[j])) numOfIntersections++;
        }
    }

    std::cout << "Number of intersections within test range: " << numOfIntersections << std::endl;

    return 0;
}