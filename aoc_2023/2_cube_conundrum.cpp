#include <iostream>
#include <sstream>
#include <unordered_map>
#include <cctype>
#include <fstream>

std::unordered_map<char, int> bagContents {
    {'r', 12},
    {'g', 13},
    {'b', 14}
};

// part 1
int processGame(const std::string& line) {
    std::istringstream s(line);
    std::string placeholder, set;
    int gameNumber;

    // read game number
    s >> placeholder >> gameNumber >> placeholder;

    int count;
    std::string color;
    while (std::getline(s, set, ';')) {
        std::istringstream ss(set);
        do {
            ss >> count >> color;
            
            if (count > bagContents[color[0]]) return 0;
        } while (color[color.length()-1] == ',');
    }

    return gameNumber;
}

// part 2
int getGamePower(const std::string& line) {
    std::istringstream s(line);
    std::string placeholder, set;
    int gameNumber;

    // read game number
    s >> placeholder >> gameNumber >> placeholder;

    std::unordered_map<char, int> minimumCubesRequired {
        {'r', 0},
        {'g', 0},
        {'b', 0}
    };

    int count;
    std::string color;
    while (std::getline(s, set, ';')) {
        std::istringstream ss(set);
        do {
            ss >> count >> color;
            minimumCubesRequired[color[0]] = std::max(count, minimumCubesRequired[color[0]]);
        } while (color[color.length()-1] == ',');
    }

    return minimumCubesRequired['r']*minimumCubesRequired['g']*minimumCubesRequired['b'];
}


int main(int argc, char* argv[]) {

    std::fstream file("data/input_2_cube_conundrum.txt", std::ios::in);
    int possibleGames = 0;
    int sumOfPowers = 0;
    std::string line;
    while (std::getline(file, line)) {
        possibleGames += processGame(line);
        sumOfPowers += getGamePower(line);
    }
    std::cout << "Part 1: " << possibleGames << std::endl;
    std::cout << "Part 2: " << sumOfPowers << std::endl;
    return 0;
}